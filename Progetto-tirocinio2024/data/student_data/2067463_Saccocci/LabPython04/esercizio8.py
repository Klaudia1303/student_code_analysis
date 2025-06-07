s=input('Inserire una stringa:')
precedente=s
while s[0]!=precedente[-1]:
    precedente=s
    s=input('Inserire una stringa:')
print(precedente+' '+s)
