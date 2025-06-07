s=input('inseriswci una stringa: ')
t=input('inserisci una stringa: ')
r=input('inserisci una strina: ')
i=1
while i!=2:
    if(len(s)+len(t)==len(r)) and i!=2:
        print(s,t,r)
        i+=1
    if i!=2:
        s=input('inserisci una stringa: ')
    if(len(r)+len(t)==len(s)) and i!=2:
        print(t,r,s)
        i+=1

    if i!=2:
        t=input('inserisci una stringa: ')
    if(len(r)+len(s)==len(t)) and i!=2:
        print(r,s,t)
        i+=1
    if i!=2:
        r=input('inserisci una stringa: ')
