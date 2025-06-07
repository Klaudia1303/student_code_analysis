a=int(input('inserisci un mese valido: '))
b=int(input('inserisci un anno: '))
if(a>=1 and a<=11):
    print(a+1,b)
elif(a==12):
    print(1,b+1)
if(a<1 or a>12)==True:
    print('input non valido')
