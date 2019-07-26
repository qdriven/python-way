import subprocess

result = subprocess.call('date')
print(result)

print("\nToday is", end=" ", flush=True)
subprocess.call(['date', '-u', '+%A'])
# grep ,grep -i
cwd = subprocess.getoutput('pwd')
print(cwd)

(ls_status, ls_output) = subprocess.getstatusoutput('ls helloworld')
print(ls_status, ls_output)

## subprocess return status

ls_status = subprocess.call('ls helloworld', stderr=subprocess.DEVNULL, shell=True)
print(ls_status)
