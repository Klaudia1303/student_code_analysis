s=input('Inserisci una stringa: ')
q=input('Inserisci una stringa: ')
uguale=0
while uguale!=1:
    r=input('Inserisci una stringa: ')
    if len(s)+len(q)==len(r):
        uguale=1
        print(s,q,r)
    else:
        s=input('Inserisci una stringa: ')
        if len(q)+len(r)==len(s):
            uguale=1
            print(q,r,s)
        else:
            q=input('Inserisci una stringa: ')
            if len(r)+len(s)==len(q):
                uguale=1
                print(r,s,q)
