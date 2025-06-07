month = input('Insert month number here: ')
month= int(month)
year = input('Insert year here: ')
year= int(year)
if 1<=month<=12:
    if month==12:
        print(1,(year+1))
    else: print((month+1),year)
else: print('Input non valido')
