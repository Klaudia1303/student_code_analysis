s = input("inserisci una stringa: ")
k = 0
for i in range(len(s)):
    k = s.rfind(s[i])
    if s[i] == s[i + k]:
        print(k)
    
