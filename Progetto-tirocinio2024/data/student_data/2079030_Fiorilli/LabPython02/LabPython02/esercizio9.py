m=int(input('inserisci il mese: '))
a=int(input('inserisci l\'anno: '))
if m>12 or m<1:
    print ('input non valido')
else:
    if m==12:
        print ('1 ',a+1)
    else:
        print (m+1, a)
