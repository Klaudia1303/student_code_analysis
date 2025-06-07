s=input('inserisci stringa (stringa vuota per terminare):')
somma=1

while s!='' and 'a' not in s or 'c' not in s:
    somma+=1
    s=input('inserisci stringa (stringa vuota per terminare):')

print('totale stringhe senza a e c:',somma)
    
