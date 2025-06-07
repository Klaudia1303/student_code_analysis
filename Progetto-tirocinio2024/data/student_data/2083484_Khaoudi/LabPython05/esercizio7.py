s=input("Inserisci una stringa : ")
b=False
for i in range(len(s)):
    if(s.count(s[i])>1):
        b=True
        break
print(b)