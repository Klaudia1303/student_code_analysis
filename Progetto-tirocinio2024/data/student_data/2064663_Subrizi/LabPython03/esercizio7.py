c = input('Scegli un carattere: ')
s = input('Inserisci una stringa: ')

while s.count(c)<=2:
    s = input('Inserisci una stringa: ')

print(s.count(c))
