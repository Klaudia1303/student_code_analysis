n1=int(input('inserisci un primo valore intero maggiore di zero: '))
while n1<1:
    n1=int(input('errore, reinserisci il valore intero maggiore di zero: '))
n2=int(input('inserisci un secomndo valore intero maggiore di zero: '))
while n2<1:
    n2=int(input('errore, reinserisci il valore intero maggiore di zero: '))
for i in range (n1,0,-1):
    if n1%i==0 and n2%i!=0:
        print (i)
