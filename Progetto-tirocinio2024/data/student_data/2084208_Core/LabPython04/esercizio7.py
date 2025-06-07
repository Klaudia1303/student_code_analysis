s=input('Inserire una stringa: ')
precedente=0
i=0
while i<len(s):
    if s.count(s[i])>=precedente:
        precedente=s.count(s[i])
        lettera=s[i]
    i=i+1
print(lettera)

