month=int(input('please type a month: '))
year=int(input('please type a year: '))
if month>=1 and month<12:
    print (month+1,year)
elif month==12:
    print ('01',year+1)
else:
    print('input non valido!')
