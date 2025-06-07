s=input('inserisci una parola palindroma: ')
boo=True
a=s[:]
b=s[::-1]

if a!=b:
    while boo:
        t=input('non palindroma, inserisci una stringa palindroma: ')
        c=t[:]
        d=t[::-1]
        if c==d:
            print(len(t))
            boo=False
        else:
            boo=True
        
else:
    print(len(s))
        
        
   
   
