s=input('inserisci una stringa ')
i=0
k=0
if s!='':
    while i<len(s):
        if s.count(s[i])>=k:
            k=s.count(s[i])
            l=s[i]
        i+=1
    print(l)
