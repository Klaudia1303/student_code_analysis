n=int(input('Inserire un numero intero maggiore di 1:'))

while n>1:
    div=2
    c=0
    while div<=n/2 and c==0:
        if n%div==0:
            c+=1
        div+=1
    if c==0:
        print(n)
    n-=1
    
    
        
    
    
   
        
            
        
        
        
        
