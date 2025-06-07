s = input("Inserisci una stringa da almeno un carattere: ")
i = 0
c = ''
a = ''
trovato = 0
while i != len(s):
    c = s[i:i+1:1]
    i = i+1
    print(c)
    if ord(c) > 100:
        trovato = 1
        a = c
        i = len(s)
if trovato == 0:
    print("Stringa consumata e carattere non trovato: ")
else:
    print("Il primo carattere con codice Unicode maggiore di 100 è")
    print(a)
