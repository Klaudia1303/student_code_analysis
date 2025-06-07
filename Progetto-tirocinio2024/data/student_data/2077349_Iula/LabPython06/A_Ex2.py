s=input("Inserisci una stringa: ")
n=0
for i in range(0,len(s)):
    if s[i]==s[(-1)*(i+1)]:
        n+=1
    else:
        break
print(n)
        
