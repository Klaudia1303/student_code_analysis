c = input('Inserisci un carattere: ')
k = True
while k == True:
    s = input('Inserisci una stringa: ')
    s.count(c)
    if s.count(c)>2:
     print(s.count(c))
     k = False
    
