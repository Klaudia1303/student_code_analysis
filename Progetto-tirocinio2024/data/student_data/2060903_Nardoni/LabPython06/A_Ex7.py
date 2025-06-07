s1=input("Inserisci la prima stringa")
s2=input("Inserisci la seconda stringa")
parola=""
a=""
for i in range (len(s1)):
    for j in range (len(s2)):
        if s1[i]==s2[j]:
            parola=""
        for k in range(len(s2)-j):
            if s1[i+k]==s2[j+k]:
                parola+=s1[i+k]
            else:
                break
            if len(parola)>len(a):
                a=parola
print(a)
