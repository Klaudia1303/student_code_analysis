s=int(input('inserire lunghezza lato: '))
for i in range(s):
    for j in range(s):
        if i==0 or i==s-1:
            print('*',end='')
        elif j==0 or j==s-1:
            print('*', end='')
        elif j==i or j==s-1-i:
            print('*',end='')
        else:
            print(' ',end='')
    print()
    

    