s=input("Inserisci una stringa: ")
s1=input("Inserisci una stringa: ")
while len(s)!=len(s1):
      s=input("Inserisci una stringa: ")
      s1=input("Inserisci una stringa: ")
finale=""
for i in range(len(s)):
    finale+=s[i]+""+s1[i]
print(finale)
