s1=input('Inserisci una stringa ')
s2=input('Inserisci una seconda stringa ')
s1=s1+' '
mass=0
for i in range (max(len(s1),len(s2))):
    for j in range (-1,-1*max(len(s1),len(s2)),-1):
        if s1[i:j] in s2:
            if len(s1[i:j])>=mass:
                mass=len(s1[i:j])
                iniz=i
                fin=j

                
print(s1[iniz:fin])
