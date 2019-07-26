# -*- coding:utf-8 -*-
import subprocess

completed = subprocess.run(['ls','-l'])

print('return_code:',type(completed.returncode))
print('return_code:',completed.returncode)


echo_result = subprocess.run('echo $HOME',shell=True)
print('returncode:', echo_result.returncode)


echo_result = subprocess.call('echo $HOME',shell=True)
print('returncode:', echo_result)