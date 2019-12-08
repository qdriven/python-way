
from datetime import datetime,timedelta

current_date = datetime.now()
print(current_date)

one_day_delta = timedelta(days=1)
print(one_day_delta)
one_day_before = current_date-one_day_delta
print(one_day_before)

# format date 
formatted_current_date = datetime.strptime('01/09/2019','%d/%m/%Y')
print(formatted_current_date)


one_week = timedelta(weeks=1)
one_week_after = current_date+one_week
print(str(one_week_after))

## how to format date time in different formats
## how to use timezone for different timezone
## how to convert long/timestamp to data or vise/visa