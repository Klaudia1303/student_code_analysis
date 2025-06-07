s=input("Inserisci una stringa: ")
distanza_max=0
conta=0
for i in range(len(s)):
    conta=s.count(s[i])
    if(conta>=2):
        a=s.find(s[i])
        b=s.rfind(s[i])
        distanza=b-a
        if(distanza>distanza_max):
            distanza_max=distanza
print(distanza_max)