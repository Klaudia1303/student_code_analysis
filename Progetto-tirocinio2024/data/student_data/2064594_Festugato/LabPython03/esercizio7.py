i = 0
c = input('inserisci un carattere: ')
while i >= 0:
    s = input('inserisci una stringa: ')
    if s.count(c) >= 2:
        print(s.count(c))
        break
    i+=1
        
        
