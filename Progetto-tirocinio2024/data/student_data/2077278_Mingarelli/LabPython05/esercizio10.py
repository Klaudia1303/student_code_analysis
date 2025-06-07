l=int(input('inserisci un lato'))
for i in range(l):
    for j in range(l):
        if i==0 or i==l-1 or j==0 or j ==l-1 or j==i or j==l-1-i:
            print('*',end='')
        else:
            print(' ',end='')
    print('')
