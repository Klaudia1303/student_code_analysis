n=int(input('Inserisci un numero intero n>=0: '))
if n==0 or n==1:
    print(1)
elif n==2:
    print(2)
x=n
fattoriale=1
while n>1 and x>1:
    fattoriale=fattoriale*x
    x=x-1
if n>2:
    print(fattoriale)