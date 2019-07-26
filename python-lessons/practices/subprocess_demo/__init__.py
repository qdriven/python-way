# -*- coding:utf-8 -*-

"""
# subprocess: Spawning Additional Processes
Purpose:	Start and communicate with additional processes.

主要有三个高层的api：
- check_output()
- check_call()
- call()

## Popen 使用

Popen是一个底层的API，用来更加复杂的交互，Popen接收一些参数，同时
会新建一个新的进程，同时通过pipe和父进程进行交互


"""