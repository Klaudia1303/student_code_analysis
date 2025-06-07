s=input('inserisci una stringa: ')
d=0

for c in s:
    dc=s.rfind(c)-s.find(c)
    if s.find(c)!=s.rfind(c) and d<dc:
        d=dc
print(d)


