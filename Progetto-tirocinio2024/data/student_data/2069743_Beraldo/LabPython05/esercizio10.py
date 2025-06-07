n=int(input('inserisci un numero'))

for m in range(1,n+1):
    for i in range (1,n+1):
        if m==1 or i==1 or m==n or i==n or m==i or (m+i)==(n+1):
            print('*',sep='',end='')
        else:
            print(' ',sep='',end='')
    print('    ')
    
