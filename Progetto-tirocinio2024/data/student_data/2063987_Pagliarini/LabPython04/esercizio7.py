s=input("inserisci una stringa ")
i=0
z=0
while i<len(s):
    if s.count(s[i])>=z:
        c=s[i]
        z=s.count(s[i])
    i+=1
print(c)
