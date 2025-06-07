s=input('Inserire una stringa: ')
i=1
massimo=s.count(s[0])
Smax=s[0]
while i<len(s):
    c=s.count(s[i])
    if c>=massimo:
        massimo=c
        Smax=s[i]
    i+=1
print(Smax)
    
