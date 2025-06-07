n=int(input("Inserire il lato del quadrato:"))
for y in range(n):
    for x in range(n):
        if x==y or x==0 or y==0 or n-x-1==y or x==n-1 or y==n-1:
            print("*",end='')
        else:
            print(' ',end='')
    print('')
            
