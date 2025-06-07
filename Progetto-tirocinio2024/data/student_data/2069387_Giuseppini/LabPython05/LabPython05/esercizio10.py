l=int(input('inserisci int >2: '))

for i in range(l):
    for c in range(l):
        if i==0 or i==(l-1) or c==0 or c==(l-1) or c==i or c==(l-1-i):
            print('*',end='')
        else:
            print(' ',end='')
    print()







