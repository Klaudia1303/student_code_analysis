humanYears=float(input('età del cane: '))
if(0<=humanYears<=2):
    print(humanYears*10.5)
elif(humanYears>2):
    print(21+(humanYears-2)*4)
else:
    print('età non valida')