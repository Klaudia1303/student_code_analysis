i=1
l=input('inserisci una stringa:')
m=input('inserisci una stringa:')
n=input('inserisci una stringa:')
while i!=2:
    if (len(l)+len(m)==len(n)) and i!=2:
        print(l,m,n)
        i+=1
    if i!=2:
      l=input('inserisci una stringa:')
    if (len(l)+len(m)==len(n)) and i!=2:
        print(l,m,n)
        i+=1
    if i!=2:
        m=input('inserisci una stringa:')
    if (len(n)+len(l)==len(m)) and i!=2:
        print(n,l,m)
        i+=1
    if i!=2:
        n=input('inserisci una stringa:')
        
