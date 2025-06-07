c=input('inserisci carattere c:')
s=input('inserisci stringa s:')
while s.count(c)<=2:
    print(s)
    s=input('inserisci stringa s:')
if s.count(c)>2:
    print(s.count(c))
    
    
