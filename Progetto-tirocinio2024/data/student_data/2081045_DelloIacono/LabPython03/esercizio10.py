n=int(input('inserire un numero intero positivo maggiore di 1: '))
i=2
while (i<=n):
    contatore=2
    while(contatore<i and i%contatore!=0):
        contatore=contatore+1
    if(contatore==i):
            print(i)
    i=i+1
