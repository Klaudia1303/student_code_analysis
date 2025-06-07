s=input("Inserire una stringa s: ")
lunghezza=len(s)
livello=0
for i in range(0,lunghezza):
    lung_2=lunghezza-1-i
    if s[i] == s[lung_2]:
        livello = livello+1
    else:
        break
print("La stringa inserita è palindroma di livello " +str(livello))
    
