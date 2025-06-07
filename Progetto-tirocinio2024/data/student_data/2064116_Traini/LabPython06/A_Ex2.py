#Diciamo che una stringa è palindroma di livello 1 se il primo e ultimo carattere sono uguali, di livello 2 se il 
#primo è uguale all’ultimo e il secondo al penultimo, e così via. Scrivere un programma Python che prende in 
#input una stringa s e calcola il livello massimo di palindromicità della stringa. Ad esempio, se la stringa s vale 
#‘alidfefcila’ allora il livello è 3. Se la stringa è palindroma allora il suo livello deve essere uguale alla sua 
#lunghezza
s=str(input('insert string: '))
p=s[::-1]
d=True
#crea una copia al contrario della stringa
LivelloPalindromicità=0
for i in range(len(s)):
    if d:
            for a in range(len(p)):
                if i==a:
                    if p[a]==s[i]:
                        LivelloPalindromicità=LivelloPalindromicità+1
                        break
                    if p[a]!=s[i]:
                        d=False
                    
                        break
print(LivelloPalindromicità)
                
        

            
            

            
            
            
            
    
    
    
    
    
        
    
    
