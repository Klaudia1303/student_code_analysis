n=int(input('inserisci un intero (0 per terminare): '))
conta=0
while n!=0:
    if n%3==0:
        conta=conta+n
    n=int(input('inserisci un intero (0 per terminare): '))
print('la somma degli interi divisibili per 3 è:',conta)
