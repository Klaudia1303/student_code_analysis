s=input('Inserisci una stringa: ')
l=input('Inserisci una stringa: ')
k=input('Inserisci una stringa: ')
i=1
while i!=2:
    if (len(s)+len(l)==len(k)) and i!=2:
        print(s,l,k)
        i+=1
    if i!=2:
        s=input('Inserisci una stringa: ')
    if (len(l)+len(k)==len(s)) and i!=2:
        print(l,k,s)
        i+=1
    if i!=2:
        l=input('Inserisci una stringa: ')
    if (len(k)+len(s)==len(l)) and i!=2:
        print(k,s,l)
        i+=1
    if i!=2:
        k=input('Inserisci una stringa: ')