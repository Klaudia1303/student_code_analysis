s = input("inserisci una stringa: ")
a = 0
for i in range(len(s)):
    if (s.rfind(s[i]) - i) > a:
        a = (s.rfind(s[i]) - i)
print(a)
    
