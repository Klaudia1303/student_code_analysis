c=input('inserisci un carattere ')
s=input('inserisci una stringa ')
while s.count(c)<=2:
    s=input('inserisci una stringa ')
if s.count(c)>=2:
    print(s.count(c))
    
