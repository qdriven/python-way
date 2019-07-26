# -*- coding:utf-8 -*-
import subprocess


def ping_master():
    args = """
       -s 10.199.192.47
       -s 10.199.192.46
       --user=root
       --master_ip=10.199.192.46
       --master_port=3306
       --user=root
       --master_ip=10.199.192.45
       --master_port=3306
       --master_user=admin
       --master_password=123456
       --ping_type=CONNECT
    """
    command = ["masterha_secondary_check", args]

    result = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    print(result.returncode)
    print(result.stdout.decode("utf-8"))