n=input('Inserisci un intero: ')
SommaNeg=0
while n!='*':
    N=int(n)
    if N<0:
        SommaNeg=SommaNeg+N
    n=input('Inserisci un intero: ')
print(SommaNeg)
