s=int(input('Inserisci un intero: '))
n=1
fattoriale=s

if s==0:
    print('1')
else:
    while s>n:
        if n>0 and s>0:
            fattoriale=fattoriale*(s-n)
        n+=1
    print(fattoriale)
