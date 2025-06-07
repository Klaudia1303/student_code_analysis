c = input("Inserisci un carattere: ")
s = ''
n = 0
while s != 'fine':
    s = input("Inserisci una stringa: ")
    n = s.count(c)
    if n > 2:
        s = 'fine'
print(n)
