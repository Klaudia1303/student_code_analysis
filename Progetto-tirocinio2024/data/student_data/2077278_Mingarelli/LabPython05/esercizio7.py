a=False
s=input('inserisci una stringa ')
for i in range(len(s)):
    if s.count(s[i])>1:
        a=True
print(a)
