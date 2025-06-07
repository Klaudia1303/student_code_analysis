s=input('inserisci una stringa: ')
d1=0
for i in range(0,len(s)):
    if s.count(s[i:i+1])>1:
        d2=s.rfind(s[i:i+1])-s.find(s[i:i+1])
        if d2>d1:
            d1=d2
print(d2)
