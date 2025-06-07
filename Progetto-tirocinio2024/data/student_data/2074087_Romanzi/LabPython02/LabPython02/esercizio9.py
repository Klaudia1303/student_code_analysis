m=int(input('Mese '))
a=int(input('Anno '))
if m<1 or m>12:
    print('Input non valido')
else:
    if m==12:
        print('1 '+str(a+1))
    else:
        print(str(m+1)+' '+str(a))
