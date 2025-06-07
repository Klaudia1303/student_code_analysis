s1=input("Inserisci una stringa: ")
s2=input("Inserisci una stringa: ")
s=""
for i in range(len(s1)+len(s2)-4):
    s+=s1[i]+s2[i]+""
print (s)
