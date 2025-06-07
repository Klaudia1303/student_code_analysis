c=input('Inserisci un carattere: ')
s=input('Inserisci una stringa: ')
i=0
while i<len(s):
    if s.count(c)>2:
        print(s.count(c))
        i=len(s)
    else:
        s=input('Inserisci una stringa: ')
