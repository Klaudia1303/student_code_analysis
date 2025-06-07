x=int(input('scrivere un numero intero tra 1 e 10: '))
y=int(input('scrivere un secondo numero intero tra 1 e 10: '))
if 0<=x<=10 and 0<=y<=10:
    i=0
    while i<=10:
        if not x==i and not y==i:
            print(i)
        i=i+1
else:
    print('x o y non sono validi')
