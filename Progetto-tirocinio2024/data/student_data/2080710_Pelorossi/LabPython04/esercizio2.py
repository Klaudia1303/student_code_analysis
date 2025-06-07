vero=True
tot=0
while vero:
    n=input('inserisci un numero intero:')
    if n=='*':
        vero=False
    elif int(n)>0:
            tot+=1
print('Il toltale dei numeri inseriti è:', tot)
    
