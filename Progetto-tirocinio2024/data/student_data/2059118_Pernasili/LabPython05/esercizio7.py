s=input("Inserisci una stringa: ")
i=0
c=1
trovato=False
ss=''
for i in range(0,len(s)):
    trovato=False
    if s.count(s[i]) > 1:
        
            trovato=True 
    
    
print(trovato)
