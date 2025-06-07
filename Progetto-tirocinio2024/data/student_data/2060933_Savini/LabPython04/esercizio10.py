s=input ('inserisci una stringa:')
l=input ('inserisci una stringa:')
m=input ('inserisci una stringa:')
i=1
while i!=2:
    if (len(s)+len(l)==len(m)) and i!=2:
        print (s,l,m)
        i+=1
    if i!=2:
        s=input('inserisci una stringa:')
    if (len (l)+len(m)==len(s)) and i!=2:
        print (s,l,m)
        i+=1
    if i!=2:
        l=input('inserisci una stringa:')
    if (len(m)+len(s)==len (l)) and i!=2:
        print (m,s,l)
        i+=1
    if i!=2:
        m=input('inserisci una stringa:')
