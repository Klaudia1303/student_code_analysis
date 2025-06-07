s=input("Inserisci una stringa")
conta=0
for i in range (len(s)):
    if s[i]==s[-i-1]:
        conta+=1
    else:
        break
if conta==0:
    print("Stringa non palindroma")
else:
    print("Stringa palindroma di livello", conta)
      
