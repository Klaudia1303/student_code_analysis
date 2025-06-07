s=input('inserisci una stringa: ')
fine=s[len(s)-1]
parola1=s
finito=False
while not finito:
    s=input('inserisci una stringa: ')
    inizio=s[0]
    parola2=s
    if fine==inizio:
        print(parola1, parola2)
        finito=True
    fine=s[len(s)-1]
    parola1=s
        
    
    
            
              
        
