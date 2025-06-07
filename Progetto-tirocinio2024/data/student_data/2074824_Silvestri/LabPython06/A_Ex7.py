s1 = input("Inserisci una stringa non vuota: ")
s2 = input("Inserisci una stringa non vuota: ")

maxStr = 0
maxSub1 = ""

for i in range(len(s1)):
    
    for j in range(len(s1)):
        sub1 = s1[i:j+1]
        
        
        
        if sub1 in s2 and len(sub1) > maxStr:
            maxStr = len(sub1)
            maxSub1 = sub1
        
            
        
print(maxSub1)
