l=int(input('Inserire lato del quadrato: '))
for i in range(l):
    if i==0 or i==l-1:
        print('*'*l,end='')
    else:
        print('*',end='')
        for j in range(l-2):
            if j==i-1 or j==l-i-2:
                print('*',end='')
            else:
                print(' ',end='')
        print('*',end='')
    print()
