uguali=False
s=input('Inserire una stringa: ')
finep=s[-1]
while not uguali:
    s1=input('Inserire una stringa: ')
    iniziop=s1[0]
    if finep==iniziop:
        print(s,s1)
        uguali=True
    else:
        s=s1
        finep=s1[-1]
