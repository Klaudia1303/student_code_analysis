c=input('inserisci carattere: ')
s=input('inserisci stringa: ')
while s.count(c)<=2: 
    s=input('inserisci stringa: ')
if s.count(c)>=2:
    print(s.count(c))
