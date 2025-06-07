a=int(input('inserire un mese tramite un numero '))
b=int(input('inserire un anno' ))
if a>12:
    print('input non valido')
if a<12:
    print(a+1, b)
elif a==12:
    print(a-11, b+1)
