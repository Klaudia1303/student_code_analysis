s = input('inserisci una stringa: ')
p = input('inserisci una stringa: ')
if s != '' and p != '':
    while s[-1] != p[0]:
        s = p
        p = input('inserisci una stringa: ')
print(s , p)
        
    
