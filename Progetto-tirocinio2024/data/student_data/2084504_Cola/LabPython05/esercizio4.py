n1=int(input('inserire un numero intero positivo: '))
n2=int(input('inserire un numero intero positivo: '))
if n1>=0 and n2>=0:
    multiplo=n1
    while multiplo < n2:
        print(multiplo)
        multiplo=multiplo+n1
else:
    print('input non valido')


