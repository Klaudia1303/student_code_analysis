s1=input("Inserisci una stringa: ")
s2=input("Inserisci una stringa: ")
b=False
s=""
for i in range(len(s1)):
    if(s2.count(s1[i])==0):
        s+=s1[i]
print(s)
