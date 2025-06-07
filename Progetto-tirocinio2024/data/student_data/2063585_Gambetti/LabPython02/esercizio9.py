x=int(input('inserisci un mese: '))
y=int(input('inserisci un anno: '))
a=int(x)+1
b=y+1
if int(x)>=1 and int(x)<=12:
    if int(x)>=1 and int(x)<12:
        print(a,' ',y)
    elif int(x)==12:
        print(1,' ',b)
else:
    print('input non valido')
