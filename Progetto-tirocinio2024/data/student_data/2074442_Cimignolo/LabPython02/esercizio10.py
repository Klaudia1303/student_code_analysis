a=float(input('inserisci età cane: '))

if a>=0:
    if a==0:
        print('0')
    elif 0<a<1:
        print(a*10.5)
    elif 1<=a<=2:
        print(a*10.5)
    else:
        print((a-2)*4 + 21)
