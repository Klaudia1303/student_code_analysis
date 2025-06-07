n=int(input("assegna un numero alla lunghezza del lato di un quadrato: "))

for i in range(n):
    for x in range(n):
        if i==0 or i==n-1:
            print('*',end='')
        elif x==0 or x==n-1:
            print('*',end='')
        elif x==i or x==n-1-i:
            print('*',end='')
        else:
            print(' ',end='')
    print()
