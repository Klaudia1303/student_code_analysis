s=input("Inserire una stringa: ")
s_ritoccata=""
vero=False
for i in range(len(s)):
    s_ritoccata=s[:i]+s[i+1:]
    contatore=0
    for x in s_ritoccata:
        if s[i]==x:
            contatore+=1
    if contatore>0:
        vero=True
print(vero)