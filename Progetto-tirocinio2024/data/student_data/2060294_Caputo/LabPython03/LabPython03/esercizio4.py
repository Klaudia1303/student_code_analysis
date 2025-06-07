x=input('inserisci un numero compreso tra 0 e 10, compresi: ')
x=int(x)
y=input('inserisci un altro numero compreso tra 0 e 10, compresi: ')
y=int(y)
n=0
while n<=10:
    if n==x:
        print('*')
    else:
        if n==y:
            print('*')
        else:
            print(n)
    n=n+1
