# -*- coding: utf-8 -*-
import time
from concurrent.futures import ThreadPoolExecutor

import requests

HTTPBIN_URL = "http://httpbin.org/get?a={}"
COUNTS = range(12)



def fetch(a):
    r = requests.get(HTTPBIN_URL.format(a))
    return r.json()['args']['a']


start = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    for num, result in zip(COUNTS, executor.map(fetch, COUNTS)):
        print("fetch({})={}".format(num, result))
        
print('Use requests+ThreadPoolExecutor cost: {}'.format(time.time() - start))
