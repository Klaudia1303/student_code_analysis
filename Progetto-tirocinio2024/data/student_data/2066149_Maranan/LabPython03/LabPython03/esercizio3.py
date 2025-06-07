n = int(input('Inserisci un numero intero qualsiasi oppure uno divisibile per 5 per\
 terminare: '))

while not n%5 == 0:
    n = int(input('Inserisci un altro numero intero qualsiasi oppure uno divisibile per\
 5 per terminare: '))


if n%5 == 0:
    print (int(n/5))
    
