n=int(input('inserisci un intero maggiore o uguale a 0: '))
conta=1
if n<0:
    print('valore non valido')
elif n==0 or n==1:
    print('il valore del fattoriale è 1')
else:
    for k in range (1,n+1):
        conta=conta*k
    print(conta)
        
        