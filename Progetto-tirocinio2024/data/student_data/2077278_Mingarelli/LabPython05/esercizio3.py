s=input('inserisci una stringa ')
n=input('inserisci una seconda stringa ')
d=''
for i in range (len(s)):
    if n.count(s[i])==0:
        d=d+s[i]
print(d)
