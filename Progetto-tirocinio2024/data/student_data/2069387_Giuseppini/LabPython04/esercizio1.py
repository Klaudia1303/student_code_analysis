s=input('inserisci una stringa: ')
i=True
c=1

while i:
    if s.count('c')>0 and s.count('a')>0:
        print(c)
        i=False
    else:
        c=c+1
        s=input('inserisci una stringa: ')
