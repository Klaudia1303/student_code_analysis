a=input('inserire un anno rappresentato con un numero intero: ')
a=int(a)
m=input('inserire un mese rappresentato tramite un numero intero: ')
m=int(m)
if m>=1 and m<13:
    print(m+1,a)
elif m==12:
    print(1,a+1)
else:
    print('input non valido')
