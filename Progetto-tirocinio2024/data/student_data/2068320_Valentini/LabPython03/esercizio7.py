contatore = 0
c = input('Inserire un carattere: ')
while contatore <= 2:
    s = input('Inserire una stringa: ')
    i = 0
    lunghezza = len(s)
    contatore = s.count(c)
    if contatore > 2:
        print(contatore)
        break
    i+=1
    contatore==0
