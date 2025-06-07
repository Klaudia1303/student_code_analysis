s1=input('inserisci una stringa:')
s2=input('inserisci una stringa:')
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j] and s1[i+1]==s2[j+1]:
            print(s1[i]+s1[i+1], end='')
           
        
