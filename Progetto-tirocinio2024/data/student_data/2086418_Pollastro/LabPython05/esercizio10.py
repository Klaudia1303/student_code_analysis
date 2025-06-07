l= int(input('inserire il lato del quadrato: '))

for c in range(l):
    for j in range(l):
        if c==0 or c==l-1:
            print('*',end='')
        else:
            if j==0 or j==l-1:
                print('*',end='')
                
            elif j==c or j==l-(c+1):
                print('*',end='')
            
            else:
                print(' ',end='')


    print('\n')
