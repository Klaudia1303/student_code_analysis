s = input("Inserisci una stringa: ")
k = False
for i in range(len(s)):
     m = s.rfind(s[i])
     if i != m:
         k = True
print(k)
