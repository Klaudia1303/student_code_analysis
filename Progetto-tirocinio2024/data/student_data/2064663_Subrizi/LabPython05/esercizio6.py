s=input('Inserisci una stringa: ')
t1=0
for i in range(len(s)):
    for j in range(1, len(s)):
        if s[i]==s[j]:
            distanza=j-i
            if t1<=distanza:
                t1=distanza
print(t1)
            
    
