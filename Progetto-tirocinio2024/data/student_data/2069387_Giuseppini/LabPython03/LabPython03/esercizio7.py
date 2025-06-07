c=input('inserisci carattere: ')
i=True

while i:
    s=input('inserisci una stringa: ')
    if s.count(c)>2:
        print(s.count(c))
        i=False

