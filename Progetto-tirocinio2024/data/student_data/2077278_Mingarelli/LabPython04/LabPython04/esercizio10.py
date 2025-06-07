s=input('inserisci una stringa ')
n=input('inserisci una stringa ')
d=input('inserisci una stringa ')
i=1
while i!=2:
    if (len(s)+len(n)==len(d)) and i!=2:
        print(s,n,d)
        i+=1
    if i!=2:
        s=input('inserisci una stringa ')
    if (len(n)+len(d)==len(s)) and i!=2:
        print(n,d,s)
        i+=1
    if i!=2:
        n=input('inserisci una stringa ')
    if (len(d)+len(s)==len(n)) and i!=2:
        print(d,s,n)
        i+=1
    if i!=2:
        d=input('inserisci una stringa ')
    
