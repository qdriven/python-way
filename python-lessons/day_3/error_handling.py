x = 42
y = 206
if x == y:
    print('Success')

z = 0
try:
    print(x / z)
except ZeroDivisionError as e:
    # Optionally, log e somewhere
    print('Sorry, something went wrong')
except:
    print('Something really went wrong')
finally:
    print('This always runs on success or failure')
