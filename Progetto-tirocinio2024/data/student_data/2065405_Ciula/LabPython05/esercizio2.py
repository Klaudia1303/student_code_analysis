s1=input("Inserisci una stringa: ")
n=int(input("Inserisci un numero: "))
s=""
for i in range(len(s1)):
    s+=s1[i]*n
print(s)
