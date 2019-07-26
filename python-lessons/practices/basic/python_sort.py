# -*- coding: utf-8 -*-

result = [{"activeTime": 1234532}, {"activeTime": 2345}]

# result.sort()

# print(result.sort())

print(sorted(result, key=lambda item: item['activeTime']))
print(sorted(result,reverse=True, key=lambda item: item['activeTime']))
