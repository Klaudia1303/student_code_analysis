a=input('inserisci un mese valido:')
b=input('inserisci un anno:')
A=int(a)
B=int(b)
if(A>=1 and A<=11)==True:
    print(A+1,B)
if(A==12)==True:
    A=1
if(A==1)==True:
    print(A,B)
if(A<1 or A>12)==True:
    print('input non valido')
