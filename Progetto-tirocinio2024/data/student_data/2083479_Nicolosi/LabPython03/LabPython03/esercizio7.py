c=input('Inserisci un carattere: ')
s=input('Inserisci una stringa: ')
numero=s.count(c)
while numero <=2:
    s=input('Inserisci una stringa: ')
    numero=s.count(c)
if numero>2:
    print(numero)