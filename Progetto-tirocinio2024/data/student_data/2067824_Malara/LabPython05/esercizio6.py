s=input('inserire una stringa: ')
precedente=0
for i in s:
    if s.count(i)>1:
        i2=s.rfind(i)
        if len(s[s.find(i):i2])>precedente:
            precedente=len(s[s.find(i):i2])
print(precedente)
        
