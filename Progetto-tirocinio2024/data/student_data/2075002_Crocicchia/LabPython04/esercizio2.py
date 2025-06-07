n=input('inserisci un intero (* per terminare): ')
conta=0
while n!= '*':
    n=int(n)
    if n >=0:
        conta+=1
    n=input('inserisci un intero (* per terminare): ')
print('sono stati inseriti',conta,'interi positivi')
