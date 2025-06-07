year=int(input('please type any year: '))
leapYear=(year%4==0 and year%100!=0) or year%400==0
if leapYear==True:
    print(year, 'is or was a leap year')
else:
    print(year, 'isn\'t or wasn\'t a leap year')
