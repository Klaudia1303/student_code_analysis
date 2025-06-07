s1=input("Inserisci una stringa")
s2=input("Inseriscine un'altra")
for i in range (len(s1)):
    if s1[i]!=s2[i] and s2.find(s1[i])==-1:
        print(s1[i],end="")
