n=input('inserisci un intero (* per terminare): ')
conta=0
while n!= '*':
    n=int(n)
    if n <=0:
        conta=conta+n
    n=input('inserisci un intero (* per terminare): ')
print('la somma degli interi negativi è:',conta)