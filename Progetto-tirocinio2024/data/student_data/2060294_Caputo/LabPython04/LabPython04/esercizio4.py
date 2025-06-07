num=int(input('inserisci un numero intero (0 per terminare): '))
i=0
while num!=0:
    if num%3==0:
        i=i+num
        num=int(input('inserisci un numero intero (0 per terminare): '))
    else:
        num=int(input('inserisci un numero intero (0 per terminare): '))
print('la somma dei numeri divisibili per 3 vale: ',i)

