num=input('inserisci un numero intero (* per terminare): ')
i=0
while num!='*':
    if int(num)>0:
        num=input('inserisci un numero intero (* per terminare): ')
        i=i+1
    else:
        num=input('inserisci un numero intero (* per terminare): ')
print('sono stati inseriti ', i,' numeri positivi')
