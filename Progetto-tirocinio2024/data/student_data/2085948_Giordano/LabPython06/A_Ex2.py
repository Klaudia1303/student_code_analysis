s=str(input("Inserisci una stringa: "))
lun=len(s)
livello=0
for i in range(0,lun):
    for j in range(lun,0):
        if s[i]==s[lun-j]:
            livello += 1

print("Stringa palindroma di livello ",livello)

   