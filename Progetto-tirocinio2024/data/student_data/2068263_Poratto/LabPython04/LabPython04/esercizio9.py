c=0
x,y,z=1,1,0
a=int(input('inserisci intero: '))
if a>0:
    if a==1:
        print(x)
        print(y)
    else:
        print(x)
        print(y)
        while c!=a-2:
            z=x+y
            print(z)
            y=x
            x=z
            z=0
            c+=1
else:
        print('intero maggiore di 0')
            
            
            
            
            
            
            
            
            
            
    
    
