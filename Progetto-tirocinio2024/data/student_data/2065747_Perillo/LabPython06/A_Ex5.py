s=input("inserisci una stringa:")
n=0
a=""
for i in range(len(s)):
    if s.count(s[i])>=n:
        n=s.count(s[i])
        a=s[i]
print(a,n)
    





