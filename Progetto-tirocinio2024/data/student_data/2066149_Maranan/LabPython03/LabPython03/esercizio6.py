s = input('Inserire una stringa: ')
i = 0
l = len(s)

while i < l and ord(s[i]) <= 100:

    i = i + 1
    
if i == l:

        print ('stringa consumata e carattere non trovato')

    

elif ord(s[i]) > 100:
        
        print ('Il primo carattere con codice Unicode maggiore di 100 è', s[i])
    
