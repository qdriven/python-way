price = 5.0
if price >= 1.00:
    tax = .07
else:
    tax = 0
# the print statement below is not indented so is executed after the if 
# statement is evaluated
print(tax)

country = 'CANADA'
# by converting the string entered to lowercase and comparing it to a string
# that is all lowercase letters I make the comparison case-insensitive
# If someone types in CANADA or Canada it will still be a match
if country.lower() == 'canada':
    print('Hello eh')
else:
    print('Hello')

province = input("What province do you live in? ")
tax = 0

if province == 'Alberta':
    tax = 0.05
elif province == 'Nunavut':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
print(tax)

country = input("What country do you live in? ")

if country.lower() == 'canada':
    province = input("What province/state do you live in? ")
    if province in ('Alberta', \
                    'Nunavut', 'Yukon'):
        tax = 0.05
    elif province == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.0
print(tax)

province = input("What province do you live in? ")
tax = 0
if province == 'Alberta' \
        or province == 'Nunavut':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
print(tax)
