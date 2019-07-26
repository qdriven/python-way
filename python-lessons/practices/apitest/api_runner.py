# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import time

from base import assert_equal, set_dictvalue, get_value_bydictpath, render_test_data, get_ksid
from base.env import target_env
from base.testrail.case_collector import CaseCollector, CaseStep, TestResultStep
from base.utils.dbwrapper import DBWrapper


class BaseTest:
    def setup_method(self, method):
        """
        Setup method for testing,init test_context,case collector
        :param method:
        :return:
        """
        print("start testing ", method.__name__)
        self.test_context = {}
        # todo for different projects
        module_name = method.__module__.replace('pytests.', "").strip()  # default to Master
        self.case_collector = CaseCollector(method_name=method.__name__)
        self.case_collector.start_test_run()

    def teardown_method(self, method):
        # collect the test result
        """
        tear down method of every test
        :param method:
        :return:
        """
        self.case_collector.collect()

    def run_test_steps(self, ksid: object, test_steps: object, step_interval_time: object = 0, ignore_assertion: object = False) -> object:
        """
        :param ksid: ksid
        :param test_steps:  测试步骤定义
        :param step_interval_time: : 每步执行的间隔时间
        :return: return all responses in test steps
        """
        response_returned = {}
        if test_steps is None:
            return

        for api, test_case_data in test_steps:
            post_data, expected_data = self.process_pre_action(test_case_data)
            if isinstance(api, DBWrapper):
                response = FakeResponse(content=api.api_call(params=post_data))
            else:
                try:
                    api_instance = api(params=post_data, ksid=ksid)
                except TypeError:
                    api_instance = api(params=post_data)
                response = api_instance.api_call()
                print("response: %s" % response.json())
            response_returned[api] = response.json()
            test_result = assert_equal(expected_data, response)
            self.process_post_action(test_case_data, response)
            time.sleep(step_interval_time)
            self.collect_testcases_data(api, api_instance, expected_data, response_returned, test_result)
            if not ignore_assertion:
                    assert test_result
        return response_returned

    def collect_testcases_data(self, api, api_instance, expected_data, response_returned, test_result):
        self.case_collector.add_case_step(
            CaseStep(api_requests=api_instance.case_step_content, expected=expected_data))
        self.case_collector.add_result_step(
            TestResultStep(api_requests=api_instance.case_step_content,
                           response_content=response_returned[api], expected=expected_data
                           , status=test_result))

    def run_tests(self, test_data={}, step_interval_time=0, ignore_assertion=False):
        """
        :param test_data:测试数据
        :param step_interval_time: 测试步骤间隔时间
        :return: all responses in test steps
        """
        if target_env.profile not in test_data['env']:
            return
        self.case_collector.title = test_data['description']
        self.case_collector.add_case_step(CaseStep(api_requests={"username": test_data["username"],
                                                                 "password": test_data["password"]}))
        ksid = get_ksid(test_data['username'], password=test_data['password'])
        return self.run_test_steps(ksid=ksid, test_steps=test_data.get('test_steps'),
                                   step_interval_time=step_interval_time,
                                   ignore_assertion=ignore_assertion)

    def process_pre_action(self, test_case_data):
        """
        pre_action structure : {
            "path_in_params or expected, in expected, start with expected":"path_in_test_context"
        }
        process pre action handler
        :param test_case_data:
        :return: post_data and expected_data
        """
        post_data = test_case_data.get('params')
        pre_action = test_case_data.get('pre_action')
        expected_data = test_case_data.get('expected')
        post_data = render_test_data(post_data, self.test_context)
        if expected_data is not None:
            expected_data = render_test_data(expected_data, self.test_context)

        self.build_data_with_pre_action(pre_action=pre_action, source_data=[post_data, expected_data])
        return post_data, expected_data

    def build_data_with_pre_action(self, pre_action, source_data=[]):
        """
        :param source_data: default is []
        :param pre_action,
        :return:
        """
        if len(source_data) == 0:
            return
        if pre_action is None:
            return
        for source in source_data:
            if source:
                for path in pre_action:
                    set_dictvalue(source, path, get_value_bydictpath(self.test_context, pre_action[path]))

    def process_post_action(self, test_case_data, response):
        """
        process post action handle
        :param test_case_data:
        :param response:
        :return:
        """
        callback = test_case_data.get('post_action')
        if callback:
            for k, v in callback.items():
                if v.startswith('result'):
                    json_response = response.json()
                else:
                    if response.json().get('result') is None:
                        json_response = response.json()
                    else:
                        json_response = response.json().get('result')
                self.test_context[k] = get_value_bydictpath(json_response, v)

    def run_test(self, api, test_data, ignore_assertion=False):

        """
        run single test
        :param api:
        :param test_data:
        :param ignore_assertion: if set to true, ignore assertion
        :return:
        """
        if target_env.profile not in test_data['env']:
            return
        self.case_collector.title = test_data['description']
        self.case_collector.add_case_step(CaseStep(api_requests={"username": test_data["username"],
                                                                 "password": test_data["password"]}))
        ksid = get_ksid(test_data['username'], password=test_data['password'])
        self.case_collector.add_result_step(
            TestResultStep(api_requests={"username": test_data["username"],
                                         "password": test_data["password"]},
                           response_content={"ksid": ksid}, expected=test_data.get('expected')
                           , status=True))

        api_instance = api(params=test_data.get('params'), ksid=ksid)
        response = api_instance.api_call()
        print("response: %s" % response.text)
        test_result = assert_equal(test_data.get('expected'), response)

        self.case_collector.add_case_step(
            CaseStep(api_requests=api_instance.case_step_content, expected=test_data.get('expected')))
        self.case_collector.add_result_step(
            TestResultStep(api_requests=api_instance.case_step_content,
                           response_content=response.json(), expected=test_data.get('expected')
                           , status=test_result))

        if not ignore_assertion:
            assert test_result
        return response
