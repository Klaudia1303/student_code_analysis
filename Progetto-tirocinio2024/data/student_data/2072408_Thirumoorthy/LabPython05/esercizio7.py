s=input('inserire stringa: ')
risultato=False
for c in s:
    if s.count(c)>1:
        risultato=True
    else:
        risultato=False
        
print(risultato)
    
    
