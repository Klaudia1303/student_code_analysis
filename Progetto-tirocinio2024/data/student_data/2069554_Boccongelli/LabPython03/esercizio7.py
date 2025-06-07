c = input('Inserisci un carattere: ')

finito = False
while (not finito):
    s = input('Inserisci una stringa: ')
    if (s.count(c) > 2):
        finito = True
        print(s.count(c))
