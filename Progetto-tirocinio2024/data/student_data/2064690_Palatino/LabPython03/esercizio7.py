c=input('inserisci un carattere: ')
s=input('inserisci una stringa: ')
while not s.count(c)>2:
    s=input('inserisci una stringa: ')
print(s.count(c))
