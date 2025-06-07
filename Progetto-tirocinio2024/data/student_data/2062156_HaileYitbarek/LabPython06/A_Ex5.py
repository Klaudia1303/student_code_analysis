s=input('inserire una stringa non vuota: ')
conto=0
for i in range(len(s)):
    if s.count(s[i])>conto:
        conto=s.count(s[i])
for i in range(len(s)-1,-1,-1):
    if s.count(s[i])>=conto:
        print(s[i],conto)
        break
