i=0
while i<10:
    s=input("Inserisci una stringa: ")
    i+=1
    print (s[0]+s[len(s)-1])
    if s.isalpha()==True and s.islower()==True:
        break
    
        
