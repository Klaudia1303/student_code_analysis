s=input('Inserisci una stringa alfanumerica: ')
massimo=s.count(s[0])
for i in range (len(s)-1):
    if s[i]==s[i+1]:
        if s.count(s[0])<s.count(s[i]):
            massimo=s[i]
print(massimo,s.count(massimo))
            
    

        
        
