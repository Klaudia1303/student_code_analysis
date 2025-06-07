s1=input('Inserisci una stringa: ')
s2=input('Inserisci una stringa: ')
n=int(input('Inserisci un intero: '))
finale=''

for i in range(len(s1)):
    
    if s1[i] in s2:
        posizione=s1.find(s1[i])
        
        if (s1[i] in s2[posizione-n:posizione]) or (s1[i] in s2[posizione:posizione+n+1]):
            finale+=s1[i]
            
print(finale)
