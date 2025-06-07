n=int(input('Inserisci un numero intero (divisibile per 5 per terminare): '))
while n%5!=0:
    n=int(input('Inserisci un numero intero (divisibile per 5 per terminare): '))
    if n%5==0:
        print(n//5)
