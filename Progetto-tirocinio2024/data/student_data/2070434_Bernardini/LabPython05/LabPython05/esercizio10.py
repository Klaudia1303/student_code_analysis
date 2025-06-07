b=int(input('inserire lato del quadrato: '))
for i in range(b):
    for j in range(b):
        if i==j or i+j==b-1 or i==0 or j==0 or i==b-1 or j==b-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
            

    
