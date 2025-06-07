c=input('inserisci un carattere: ')
s='abcd'
while s.count(c)<=2:
    s=input('inserisci una stringa: ')
    if s.count(c)>2:
        print(s.count(c))
 
