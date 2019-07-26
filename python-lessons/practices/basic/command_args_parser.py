#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re

curl_command = """
    curl 'https://app-api.shop.alpha.elenet.me/order/invoke/?method=refundOrder.getUnprocessedRefundingOrders' -H 'Origin: http://evil.com/' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36' -H 'Content-type: application/json;charset=UTF-8' -H 'Accept: */*' -H 'Referer: http://melody.shop.alpha.elenet.me/app/shop/72308810/today/processing' -H 'Connection: keep-alive' --data-binary '{"id":"7763b700-c079-4eef-95ff-87132cd619d2","method":"getUnprocessedRefundingOrders","service":"refundOrder","params":{"restaurantId":72308810},"metas":{"appName":"melody","appVersion":"4.4.0","ksid":"SG97NUVvNvB3kIaM2zEpg9CwritT5Nb4injg"},"ncp":"2.0.0"}' --compresse
"""

## getting module name
## getting params name

matcher_obj = re.search(r'.me/(.*)/invoke/', curl_command)
matcher_obj2 = re.search(r' --data-binary (.*) --', curl_command)
print(matcher_obj.group(0))
print(matcher_obj.group(1))
print(matcher_obj2.group(0))
print(matcher_obj2.group(1))
print(eval(matcher_obj2.group(1)))

curl_command.strip()

