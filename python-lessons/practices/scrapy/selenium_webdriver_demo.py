# -*- coding: utf-8 -*-
import os
import threading

from selenium import webdriver
from selenium.webdriver.common.proxy import ProxyType


def start_up():
    driver_path = os.path.join(os.getcwd(), "chromedriver")
    driver = webdriver.Chrome(executable_path=driver_path)
    # driver = webdriver.Chrome()
    proxy = webdriver.Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = '219.234.5.128:3128'
    usl_list = ["https://cd.5i5j.com/ershoufang/40191490.html",
                "https://cd.5i5j.com/ershoufang/41897614.html",
                "https://cd.5i5j.com/ershoufang/39833575.html",
                "https://cd.5i5j.com/ershoufang/41885621.html",
                "https://cd.5i5j.com/ershoufang/30060837.html1",
                "https://cd.5i5j.com/ershoufang/31246663.html"]
    for i in range(10):
        for url in usl_list:
            driver.get(url)

    driver.close()


def print_index(start_index, end_index, list_nums):
    for i in range(start_index, end_index):
        print(threading.currentThread().getName(), i, list_nums[i])


list_num = [1, 2, 3, 4, 5, 6]
thread_num = 7
start_index = 0
end_index = 0
total_num = len(list_num)
count_per_thread = int(total_num / thread_num) if total_num > thread_num else total_num
# print(count_per_thread)
#
while start_index < total_num:
    end_index = start_index + count_per_thread
    if end_index >= total_num:
        end_index = total_num
    t = threading.Thread(target=print_index, args=(start_index, end_index, list_num),
                         name="thread-from-index-" + str(start_index))
    t.start()
    start_index = end_index

# print_index(0,1,list_num)
# print_index(1,2,list_num)
