n = int(input('Inserisci un numero intero positivo maggiore di 1: '))
i = 2
while i<=n:
    m=2
    while i%m!=0 and m<i:
        m +=1
    if i==m:
        print(i,'è un numero primo')
    i += 1
