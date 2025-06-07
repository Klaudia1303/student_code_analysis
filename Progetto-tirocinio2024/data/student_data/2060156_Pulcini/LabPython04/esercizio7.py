s=input('inserire una stringa:')
i=0
m=0
while i<len(s):
    if s.count(s[i])>=m:
        m=s.count(s[i])
        lettera=s[i]
    i+=1
print(lettera)
    
