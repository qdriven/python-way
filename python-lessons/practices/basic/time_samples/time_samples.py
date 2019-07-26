# -*- coding: utf-8 -*-
import datetime

print(datetime.datetime.now().strftime('%s'))
print(datetime.datetime.utcnow().strftime('%s'))
print(datetime.datetime.fromtimestamp(1465228800))


def get_date_timestamp(interval_day=0):
    today = datetime.date.today()
    return_date = today + datetime.timedelta(days=interval_day)
    return float(return_date.strftime("%s"))

print(datetime.datetime.fromtimestamp(get_date_timestamp(0)))
print(datetime.datetime.fromtimestamp(get_date_timestamp(-1)))
print(datetime.datetime.fromtimestamp(get_date_timestamp(1)))


print(datetime.datetime.now().timestamp())
