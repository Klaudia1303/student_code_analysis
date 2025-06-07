dogYear=float(input('please type your dog\'s age: '))
dogYearPuppy=10.5
if dogYear>=0:
    if dogYear>=0 and dogYear<=2:
        print(dogYearPuppy*dogYear)
    if dogYear>2:
        print(dogYearPuppy*2+(dogYear-2)*4)
else:
    print('please type a valid number (must be greater than or equal to 0)')
        
