s=input('Inserisci una stringa: ')
occ=1
occdef=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        occ+=1
        if occ>=occdef:
            occdef=occ
            lettera=s[i]
    else:
        occ=1
print(lettera,occdef)
