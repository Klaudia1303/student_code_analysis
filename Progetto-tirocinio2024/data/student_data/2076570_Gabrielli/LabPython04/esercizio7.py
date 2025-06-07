s=input('inserisci una stringa: ')
M=0
i=0
while i<len(s):
    if s.count(s[i])>=m:
        m=s.count(s[1])
        posizione=i
    i+=1
print(s[posizione])
