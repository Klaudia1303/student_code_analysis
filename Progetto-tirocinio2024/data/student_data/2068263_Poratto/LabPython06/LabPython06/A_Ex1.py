x,y=int(input('inserisci intero: ')),int(input('inserisci un altro intero: '))
for i in range(x+1,1,-1):
    if x%i==0:
        if y%i==0:
            continue
        print(i)
            
        
    
