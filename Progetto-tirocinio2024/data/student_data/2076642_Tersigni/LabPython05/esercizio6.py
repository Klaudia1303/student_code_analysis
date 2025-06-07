s=input("inserisci una stringa")
c=0
for i in range(len(s)):
    if s.rfind(s[1])-s.find(s[i])>c:
        c=s.rfind(s[1])-s.find(s[1])
print(c)
