c=input('Inserisci un carattere: ')
i=0
while i==0:
    s=input('Inserisci una stringa: ')
    if s.count(c)>2:
        print('Il carattere è presente nella stringa: ',s.count(c))
        i=1
