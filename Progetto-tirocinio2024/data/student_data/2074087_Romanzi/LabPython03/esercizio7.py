s=True
while s:
    c=str(input('Carattere '))
    if len(c)==1:
        s=False
    else:
        print('Input non valido ')
o=True
while o:
    p=str(input('Stringa da controllare '))
    if p.count(c)>2:
        print(p.count(c))
        o=False
        
