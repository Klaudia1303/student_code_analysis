num=input('inserisci un numero intero (* per terminare): ')
i=0
while num!='*':
    if int(num)<0:
        i=i+(int(num))
    num=input('inserisci un numero intero (* per terminare): ')

print('la somma dei numeri negativi che hai inserito vale:', i)

