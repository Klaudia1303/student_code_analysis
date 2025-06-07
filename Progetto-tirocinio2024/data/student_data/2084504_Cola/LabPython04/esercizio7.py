s=input('scrivere una stringa: ')
i=0
y=0
if s!='':
    magg=s[i]
    while i<len(s):
        x=s.count(s[i])
        if x>=y:
            y=x
            magg=s[i]
        i=i+1
    print(magg)
else:
    print('input non valido')

