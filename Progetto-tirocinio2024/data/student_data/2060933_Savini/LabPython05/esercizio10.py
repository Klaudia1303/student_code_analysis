n=int (input ('inserisci un numero: ') )
for i in range (n) :
    for c in range(n):
        if i==0 or i==n-1:
            print ('*',end='')
        elif c==0 or c==n-1:
            print ('*',end='')
        elif c==i or c==n-1-i:
            print ('*',end='')
        else:
            print(' ',end='')
    print()
