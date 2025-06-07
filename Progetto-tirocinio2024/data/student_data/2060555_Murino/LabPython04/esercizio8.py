i=0
cn=0
while i!=1:
    while cn<1:
        s=input('inserisci una stringa non vuota: ')
        c= str(s)
        k= str(' ')
        cn+=1
        while cn>=1 and i!=1:
            sc=input ('inserisci una stringa non vuota: ')
            k= str(sc)
            if k[0]==c[-1]:
                print(c,k)
                i+=1
            s=input('inserisci una stringa non vuota: ')
            c= str(s)
            if k[-1]==[0]:
                print(k,c)
                i+=1
