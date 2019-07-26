# -*- coding: utf-8 -*-
import asyncio

import time
from concurrent.futures import ThreadPoolExecutor

import requests

HTTPBIN_URL = "http://httpbin.org/get?a={}"
COUNTS = range(12)


def fetch(a):
    r = requests.get(HTTPBIN_URL.format(a))
    return r.json()['args']['a']


async def run_task(executor):
    loop = asyncio.get_event_loop()
    blocking_tasks = []
    for num in COUNTS:
        task = loop.run_in_executor(executor, fetch, num)
        task.__num = num
        blocking_tasks.append(task)
    completed, pending = await asyncio.wait(blocking_tasks)
    results = {t.__num: t.result() for t in completed}
    for num, result in sorted(results.items(), key=lambda x: x[0]):
        print('fetch({})={}'.format(num, result))


start = time.time()
executor = ThreadPoolExecutor(max_workers=3)
event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(
    run_task(executor)
)

print('use async io cost : {}'.format(time.time()-start))
