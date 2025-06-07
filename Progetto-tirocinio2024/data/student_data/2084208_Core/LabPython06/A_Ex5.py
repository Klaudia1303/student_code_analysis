s=input('Inserire una stringa: ')
precedente=0
for i in range (0,len(s)):
    conto=s.count(s[i])
    if s.count(s[i])>s.count(s[precedente]):
        precedente=i
    else:
        precedente=precedente
    if s.count(s[i])==s.count(s[precedente]):
        precedente=max(i,precedente)
print(s[i],s.count(s[i]))
        
    
    
    
