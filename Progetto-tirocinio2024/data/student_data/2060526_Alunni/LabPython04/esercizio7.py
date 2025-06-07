s = str(input('inserisci una stringa: '))
if s!='':
    l=s[0]
    x=s.count(l)
    y=1
    while y!=(len(s)):
        m=s[y]
        t=s.count(m)
        if t>x:
            l=m
        y=y+1
    print (l)
