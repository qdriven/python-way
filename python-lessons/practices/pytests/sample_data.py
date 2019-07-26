#!/usr/bin/env python
# -*- coding: utf-8 -*-

LOGIN_INFO = {
    "protocol": "old_vine",
    "appName": "melody",
    "appVersion": "4.4.0",
    "type": "invoke.request",
    "method": "secure.login.loginByUsername",
    "params": {
        "username": "alice5",
        "password": "eleme517517"
    },
    "ncp": "1.0.0"
}

# 获取营销推广活动
GET_APPLY_ACTIVITY = {
    "protocol": "vine",
    "appName": "melody",
    "appVersion": "4.4.0",
    "type": "invoke.request",
    "method": "getApplyActivity",
    "service": "applyActivityManage",
    "params": {
        "shopId": 74753461
    },
    "ncp": "2.0.0"
}

if __name__ == '__main__':
    items = locals()
    for item in locals():
        print(items)
