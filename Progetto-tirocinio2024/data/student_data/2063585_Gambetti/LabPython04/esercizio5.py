n=int(input('inserisci un intero maggiore o uguale di 0: '))
i=1
somma=1
finito=False
while n>1 and i<=n:
    s=1*i
    i+=1
    somma=somma*s
print(somma)
if n=='0' or n=='1':
    print('1')
