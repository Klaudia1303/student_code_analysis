n=int(input("Inserire il lato del quadrato:"))
altezza=n
spazio=n-1
for i in range(0,altezza):
    if i==0:
        for g in range(0,n):
            print("*",end='')
    if i>0 and i<=altezza-2:
        print('')
        print('*',end='')
        for f in range(0,spazio-1):
            print(" ",end='')
        print('*',end='')
    if i==altezza-1:
        print('')
        for z in range(0,n):
            print("*",end='')

  
        
