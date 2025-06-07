s=input('inserisci una stringa: ')
livello=0
for i in range(len(s)//2):
        if s[i]==s[len(s)-i-1]:
            livello=livello+1
        else:
            break
        if livello==len(s)//2 and len(s)%2==0:
            livello=livello*2
        if livello==len(s)//2 and len(s)%2==1:
            livello=livello*2+1
print(livello)
