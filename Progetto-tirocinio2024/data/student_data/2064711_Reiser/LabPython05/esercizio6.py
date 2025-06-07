s=str(input("inserisci una stringa:"))
dist=0
for i in range(0,len(s)):
    if s.rfind(s[i])-s.find(s[i])>dist:
        dist=s.rfind(s[i])-s.find(s[i])
print(dist)
