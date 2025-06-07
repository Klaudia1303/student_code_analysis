s=input("Inserisci una stringa alfanumerica non vuota:")
occ=0
for i in range(len(s)):
    x=s.count(s[i])
    if x>=occ:
        occ=x
        a=s[i]
print(a, occ)
