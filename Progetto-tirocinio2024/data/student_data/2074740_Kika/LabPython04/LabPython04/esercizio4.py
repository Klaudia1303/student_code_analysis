n=int(input('inserisci intero(0 per terminare): '))
k=0
while n!=0:
    if n%3==0:
        k=k+n
    n=int(input('inserisci intero(0 per terminare): '))
print(k)
