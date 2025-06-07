s=input('inserisci una stringa: ')
i=0
m=0
c=0
while i<len(s):
    if s.count(s[i])>=m:
        m=s.count(s[i])
        c=i
    i+=1
print (s[c])
