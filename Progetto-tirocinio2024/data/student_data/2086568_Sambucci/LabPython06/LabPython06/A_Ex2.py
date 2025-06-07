s=input('Inserisci stringa: ')
j=s[::-1]
i=0
livello=0
while i<len(s):
    if s[i]==j[i]:
        livello+=1
    else:
        break
    i+=1
print('Stringa di livello',livello)
        
    
