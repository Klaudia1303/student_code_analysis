n=int(input('inserisci un numero intero (divisore di 5 per terminare):'))
while n%5!=0:
    print(n)
    n=int(input('inserisci un numero intero (divisore di 5 per terminare):'))
if n%5==0:
    print(n//5)
