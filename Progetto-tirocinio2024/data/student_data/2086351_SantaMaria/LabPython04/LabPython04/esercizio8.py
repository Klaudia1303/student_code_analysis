s=input('Inserisci una stringa: ')
uguale=0
while uguale!=1:
    q=input('Inserisci una stringa: ')
    if s[-1]==q[0]:
        uguale=1
        print(s,q)
    else:
        s=input('Inserisci una stringa: ')
        if q[-1]==s[0]:
            uguale=1
            print(q,s)
