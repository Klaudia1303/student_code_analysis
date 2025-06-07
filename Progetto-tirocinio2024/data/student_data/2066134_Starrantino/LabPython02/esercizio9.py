month = int(input('month: '))
year = int(input('year: '))

if 0 <= month <= 12:
    if month == 12:
        print(1, year+1)
    else:
        print(month+1, year)
else:
    print('input non valido')