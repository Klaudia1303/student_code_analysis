l = int(input('Inserisci la dimensione del lato: '))
for i in range(l):
    for j in range(l):
        if (i==j or (i+j==(l-1)))or((i==0)or(j==0)) or ((i==(l-1))or(j==(l-1))):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
