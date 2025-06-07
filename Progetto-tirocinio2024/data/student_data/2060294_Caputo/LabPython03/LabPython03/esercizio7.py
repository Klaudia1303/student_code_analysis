c=input('inserisci un carattere: ')
s=input('inserisci una stringa: ')
while s.count(c)<=2:
    s=input('inserisci una stringa: ')
print('la tua ultima stringa è: \'', s, '\' il carattere appare ', s.count(c), 'volte')
