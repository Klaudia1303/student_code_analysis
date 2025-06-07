c=input('Inserire un carattere:' )
s=input('Inserire una stringa:' )
i=2
while s.count(c)<=i:
    s=input('Inserire una stringa:' )
    if s.count(c)>i:
        print(s.count(c))
    i+=1
