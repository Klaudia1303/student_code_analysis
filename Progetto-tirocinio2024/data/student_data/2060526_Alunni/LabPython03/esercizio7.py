c=(input('inserisci il carattere: '))
n=(input('inserisci una sringa valida: '))
x=n.count(c)
while x<3:
    n=(input('inserisci una sringa valida: '))
    x=n.count(c)
print(x)
