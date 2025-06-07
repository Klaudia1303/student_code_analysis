n=int(input('Inserisci un intero maggiore di 0: '))
i=n
SommaFatt=1
if n!=0:
    while i>=1:
        SommaFatt=SommaFatt*i
        i=i-1
print(SommaFatt)
