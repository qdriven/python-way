# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from jinja2 import Template
from jsonpath_rw import parse
from objectpath import Tree




def capitalize_first(name):
    """
    首字母大写
    :param name:
    :return:
    """
    return name[0].capitalize() + name[1:]


def change_camel_to_under(name):
    """
    驼峰式变更为连接式
    :param name: 
    :return:
    """
    name_list = []
    for x in name:
        if x.islower():
            name_list.append(x)
        else:
            name_list.append("_%s" % x.lower())
    return ''.join(name_list)



def set_dictvalue(source_dict, path_in_dict, value):
    """

    :param source_dict:
    :param path_in_dict:
    :param value:
    :return:
    """
    paths = path_in_dict.split(".")
    if len(paths) == 1:
        try:
            if source_dict.get(paths[0]) is not None:
                source_dict[paths[0]] = value
            return
        except Exception as e:
            raise Exception(e + "请检查要找的字段路径是否正确,字段路径是" + path_in_dict)
    try:
        exp = parse(".".join(paths[:len(paths) - 1]))
        matched_items = exp.find(source_dict)
        for item in matched_items:
            if type(item.value[paths[len(paths) - 1]]) == list:
                item.value[paths[len(paths) - 1]] = [value]
            else:
                item.value[paths[len(paths) - 1]] = value
    except Exception as e:
        raise Exception(e + "请检查要找的字段路径是否正确,字段路径是" + path_in_dict)


def render_test_data(test_data, test_context):
    """

    :param test_data:
    :param test_context:
    :return:
    """
    return eval(Template(str(test_data)).render(test_context))


def get_value_bydictpath(source_dict, path_in_dict):
    """
    根据格式获取dict的value,只返回第一个匹配的数据
    :param source_dict:
    :param path_in_dict:
    :return:
    """
    if source_dict is None:
        raise Exception("source is None Type")
    if not isinstance(source_dict, dict):
        return source_dict
    try:
        if path_in_dict.startswith('$'):
            result = Tree(source_dict).execute(path_in_dict)
            return_result = []
            for item in result:
                return_result.append(item)
            return return_result if len(return_result) > 1 else return_result[0]
        else:
            exp = parse(path_in_dict)
            matched_items = exp.find(source_dict)
            return matched_items[0].value
    except Exception as e:
        print("path is " + path_in_dict + " it is not correct!", e)
        # raise Exception("path is " + path_in_dict + " it is not correct!", e)
        return None


def assert_equal(expected_response, response):
    if expected_response is None or len(expected_response) == 0:
        return True
    assert_result = True
    real_response = response.json()
    for k in expected_response:
        real_result = get_value_bydictpath(real_response, k)
        expected_result = expected_response[k]
        if not isinstance(real_result, type(expected_result)):
            real_result = str(real_result)
            expected_result = str(expected_result)
        if real_result != expected_result:
            assert_result = False
            print("字段%s的: 实际结果%s,期望结果是%s, 响应错误是%s" % (k, real_result, expected_response[k], real_response.get('error')))
    return assert_result


def get_image_hash_form_image_url(image_url):
    """
    根据image_url获取image_hash
    :param image_url:
    :return:
    """
    tmp_image_hash = image_url.replace('/', '').split('me')[1]
    image_hash = tmp_image_hash.split('.')[0]
    return image_hash
