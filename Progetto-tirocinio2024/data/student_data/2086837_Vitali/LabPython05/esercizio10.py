l=int(input("Inserisci lato del quadrato >=2: "))
for i in range(l):
    for j in range(l):
        if i==0 or i==l-1:
            print('*',end='')
        else:
            if j==0 or j==l-1:
                print('*',end='')
            elif j==i or j==l-1-i:
                print('*',end='')
            else:
                print(' ',end='')
    print()
