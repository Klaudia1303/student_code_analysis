s=input('inserisci stringa: ')
i=0
k=0
while i<len(s):
    if s.count(s[i])>=k:
        k=s.count(s[i])
        l=s[i]
    i+=1
print(l)
