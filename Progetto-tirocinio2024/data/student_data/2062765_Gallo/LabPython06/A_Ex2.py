s=input("Inserisci stringa: ")
livello=0
s_destra=""
s_sinistra=""
metà_stringa=len(s)//2
for i in range (0,(len(s)//2)):
    s_sinistra+=s[i]
    print(s_sinistra)
for j in range (len(s)-1,(len(s)//2)-1,-1):
    s_destra+=s[j]
    print(s_destra)
for k in range (0,(len(s)//2)):
    if s_sinistra[k]==s_destra[k]:
        livello+=1
if livello==metà_stringa:
    print("Palindroma")
else:
    print(livello)

        
