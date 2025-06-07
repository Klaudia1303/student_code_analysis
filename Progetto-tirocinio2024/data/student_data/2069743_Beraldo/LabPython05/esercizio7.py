s=input('inserisci una stringa')
c=0
z=False
while c<len(s):
    if s.count(s[c])>=2:
        z=True
        break
    else:
        z=False
    c+=1

print(z)
    

    
