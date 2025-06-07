s=input('inserisci una stringa:')
tot=0
for i in range(len(s)):
    if s.count(s[i])>=2:
        tot+=1


if tot>=1:
    print(True)
else:
    print(False)
