s=input('Inserisci una stringa ')
mass=0
conteggio=1

for i in range(len(s)-1):
    if s[i]==s[i+1]:
        conteggio+=1
        if conteggio>=mass:
            car=s[i]
        mass=max(conteggio,mass)
        
    elif i==len(s)-2:
        if s[i]==s[-1]:
            conteggio+=1
        mass=max(conteggio,mass)
        
    else:
        conteggio=1
        
print(car,mass)
