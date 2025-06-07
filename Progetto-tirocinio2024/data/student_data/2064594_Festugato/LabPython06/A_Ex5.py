s = input('inserisci una stringa: ')
car = ''
consecutive = 1
massimo = 0
for i in range(len(s)-1):
    #print(s[i],s[i+1])
    if s[i] == s[i+1]:
           consecutive += 1 #conta la successiva uguale
           car = s[i]
    else:
        consecutive = 1 #se diversa ritorna a 1
        
    if  consecutive > massimo:
            massimo = consecutive
            car = s[i]#salva ultimo carattere che compare di più

print(car,massimo)
        
        
    
    
        
    
        
        
        

    
    
