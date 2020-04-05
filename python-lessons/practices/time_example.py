import time
from datetime import date

print(time.asctime())
print(time.strftime("%a %d.%m",time.localtime()))

print(str(date.today()))