s=input("Inserisci una stringa: ")
b=False
for i in range(len(s)):
    if(s.count(s[i])>=2):
        b=True
print(b)
