s1=input("Inserire una stringa: ")
s2=input("Inserire un'altra stringa: ")
carattere_diverso=""
contatore=0
for i in range(len(s1)):
    for x in range(len(s2)):
        if s1[i]!=s2[x]:
            contatore+=1
    if contatore==len(s2):
        carattere_diverso=carattere_diverso+s1[i]
    contatore=0
print(carattere_diverso)