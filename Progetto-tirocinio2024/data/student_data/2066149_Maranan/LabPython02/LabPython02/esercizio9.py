m = int(input('Inserire il mese a numero: '))
a = int(input('Inserire l\'anno: '))
i = 1
if m>=1 and m<=11:
    print(m+1, a)
if m==12:
    print(i, a+1)
else:
    print('input non valido')
