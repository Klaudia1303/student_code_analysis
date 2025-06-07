n=int(input('Inserisci un intero >= di 0 '))
if n==0 or n==1:
    print ('Il fattoriale è 1')
elif n>1:
    fatt=n
    while n>1:
        fatt=fatt*(n-1)
        n-=1
print (fatt)
