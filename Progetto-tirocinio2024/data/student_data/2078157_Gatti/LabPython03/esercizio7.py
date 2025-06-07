c = input('inserisci un carattere: ')
s = input('inserisci una stringa: ')
b = True
while b:
    if s.count(c) <= 2:
        s = input('inserisci una stringa: ')
    else:
        print(s.count(c))
        b = False

