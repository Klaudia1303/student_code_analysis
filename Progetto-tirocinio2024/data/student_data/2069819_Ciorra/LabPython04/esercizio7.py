s=input("inserisci una stringa non vuota")
i=0
massimo=s.count(s[i])
maxcar=s[i]
while(i<len(s)):
    if s.count(s[i])>=massimo:
        massimo=s.count(s[i])
        maxcar=s[i]
    i=i+1
print(maxcar)
