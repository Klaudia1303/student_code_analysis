x,y,z,p=str(input('inserisci stringa: ')),str(input('inserisci stringa: ')),int(input('inserisci intero: ')),''
for i in range(len(x)):
    c=x[i]
    for pos,car in enumerate(y):
        if(car==c):
            if (x.find(car))-(y.find(c))<=z:
                p+=x[i]
print(p)
    

        
        
    
    
    
