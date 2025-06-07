
livello=0
s=input("inserisci una stinga: ")
for i in range(0,len(s)):
    if s[i]==s[-i-1]:
        livello=livello+1
    else:
        break
print(livello)
