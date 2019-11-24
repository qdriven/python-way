# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     json_utils
   Description :
   Author :        patrick
   date：          2019/11/24
-------------------------------------------------
   Change Activity:
                   2019/11/24:
-------------------------------------------------
"""
__author__ = 'patrick'

# -*- coding: utf-8 -*-
import re

# # from bidict import bidict as bidict
# import jmespath

## jsonpath:
## http://jmespath.org
## 1. json, 多个路径字段，dict()
## 2. querey 语法了解一下
## 3. json 完全比较,期望，实际, 忽略字段
# from jsonpath_rw import jsonpath, parse
from jsonpath_rw import parse

import json


class JsonUtil(object):

    def __get_paths__(self, data, result={}, path=""):

        if isinstance(data, dict):
            # if self.temp:
            #     self.temp.pop(path)
            for key, value in list(data.items()):
                newpath = path + "/" + str(key)
                # self.temp[newpath] = value
                self.__get_paths__(value, result, newpath)
        elif isinstance(data, list):
            i = 0
            # self.temp.pop(path)
            for subvalue in data:
                newpath = path + "[" + str(i) + "]"
                # self.temp[newpath] = subvalue
                self.__get_paths__(subvalue, result, newpath)
                i = i + 1
        elif isinstance(data, (str, int, float, bool)) or data == None:
            # self.temp.pop(path)
            result[path] = data
        return result

    def data_check(self, data):
        try:
            if isinstance(data, str):
                data = json.loads(data, encoding="utf-8")

            elif isinstance(data, dict):
                json.dumps(data)
        except:
            raise Exception("请检查data格式")
        return data

    def exclude_keys(self, data, key_list):
        data = self.data_check(data)
        if not isinstance(key_list, list):
            raise Exception("key_list必须是list类型")
        path_dict = self.__get_paths__(data, result={})
        for key in key_list:
            key_list = self.get_absolute_path(data, key)
            for key2 in key_list:
                path_dict.pop(key2)
        return path_dict

    def __group_by_key__(self, prefix, data):
        dict = {}
        subdict = {}
        for key, value in data.items():
            if str(key).startswith(prefix):
                subindex = str(key).index("]")
                mainkey = str(key)[:str(key).index("]") + 1]
                subkey = str(key)[str(key).index("]") - len(key) + 1:]
                if mainkey not in dict:
                    subdict = {}
                    subdict[subkey] = value
                    dict[mainkey] = subdict
                else:
                    dict[mainkey][subkey] = value
        return list(dict.values())

    def __compare__(self, dict1, dict2):
        prefixlist = []
        if len(dict1) == len(dict2):
            for key, value in list(dict1.items()):
                if not re.search(r'\[\d+\]', key):
                    try:
                        if dict2[key] == value:
                            dict1.pop(key)
                            dict2.pop(key)
                        else:
                            return False
                    except KeyError:
                        return False
                else:
                    prefix = str(key)[:str(key).index("[") + 1]
                    if prefix not in prefixlist:
                        prefixlist.append(prefix)
                        dictlist1 = self.__group_by_key__(prefix, dict1)
                        dictlist2 = self.__group_by_key__(prefix, dict2)
                        flag = 0
                        if len(dictlist1) != len(dictlist2):
                            return False
                        for item1 in dictlist1:
                            for item2 in dictlist2:
                                flag = 0
                                if not self.__compare__(item1, item2):
                                    flag = 1
                                else:
                                    dictlist2.remove(item2)
                                    break
                            if flag == 1:
                                return False
            return True
        else:
            return False

    def compare_all(self, data1, data2):
        return self.__compare__(self.__get_paths__(self.data_check(data1), result={}),
                                self.__get_paths__(self.data_check(data2), result={}))

    def compare_exclude_keys(self, data1, data2, key_list):
        return self.__compare__(self.exclude_keys(self.data_check(data1), key_list),
                                self.exclude_keys(self.data_check(data2), key_list))

    def compare_by_given_data(self, data, compare_data):
        data = self.__get_paths__(self.data_check(data), result={})
        if not compare_data or not isinstance(compare_data, dict) or re.match(r'\{[\s\S]*\{', str(compare_data)):
            raise Exception("compare_data只支持没有嵌套的dict类型")
        for key1, value1 in compare_data.items():
            flag = 0
            for key2, value2 in data.items():
                flag = 0
                if str(key2).endswith("/" + key1) and value1 == value2:
                    break
                else:
                    flag = 1
            if flag == 1:
                return False
        return True

    def get_values_by_key(self, data, key):
        if not isinstance(key, (str, int, float)) or key.isspace():
            raise Exception("keyname不能为空,并且keyname和keypath只能是字符串或数字类型")
        data = self.data_check(data)
        key = str(key) if not str(key).endswith("/") else str(key)[:-1]
        if key.startswith("/"):
            parsestr = "$" + key.replace("/", ".")
        else:
            parsestr = "$.." + key.replace("/", ".")
        jsonpath_expr = parse(parsestr)
        return [match.value for match in jsonpath_expr.find(data)]

    def get_absolute_path(self, data, key):
        keypath = []
        key = (str(key) if not str(key).endswith("/") else str(key)[:-1]).replace("[", "\\[").replace("]", "\\]")
        if not isinstance(key, (str, int, float)) and not None:
            raise Exception("keyname不能为空,并且只能是字符串或数字类型")
        data = self.__get_paths__(self.data_check(data), result={})
        for key2 in data.keys():
            if (key.startswith("/")) and re.match(r'' + key + '(\\[\\d*\\])*/', (str(key2) + "/")) or (
                    not key.startswith("/")) and re.search(r'/' + key + '(\\[\\d*\\])*/', (str(key2) + "/")):
                keypath.append(key2)
        return keypath


json_util = JsonUtil()
