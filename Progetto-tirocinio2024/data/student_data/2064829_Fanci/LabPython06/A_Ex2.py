s=input("inserisci stringa: ")
j=0
for i in range(0,len(s)):
    if s[i]==s[-i-1]:
        j=i+1
    else: break
print("stringa palindroma di livello:",j)
