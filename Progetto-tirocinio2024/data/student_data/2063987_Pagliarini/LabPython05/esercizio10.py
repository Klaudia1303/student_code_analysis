l=int(input('inserisci lato'))


for i in range(l):
    
    for k in range(l):
        if k<1 or k==(l-1) or i<1 or i==(l-1):
            print('*',end='')
        elif i==k or (l-1)-k==i:
            print('*',end='')
        else:
            print(' ',end='')
    print()
        
            
                
       
