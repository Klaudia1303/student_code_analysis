vero=True
tot=0
while vero:
    n=int(input('inserisci un numero intero:'))
    if n==0:
        vero=False
    if n%3==0:
        tot+=n
print('La somma degli interi divisibili per tre inseriti è:', tot)
    
