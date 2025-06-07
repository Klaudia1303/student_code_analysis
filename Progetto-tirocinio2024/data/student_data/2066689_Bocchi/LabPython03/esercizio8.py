s= input('inserisci una stringa palindroma: ')

while s!=s[len(s)::-1]:
    s= input('Non palindroma\ninserisci una stringa palindroma: ')
print('stringa palindroma di lunghezza', len(s))

    
