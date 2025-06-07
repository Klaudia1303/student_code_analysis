s = input('Inserire una stringa palindroma: ')
while s != s[::-1]:
    print('Non palindroma')
    s = input('Inserire una stringa palindroma: ')
print('Stringa palindroma di lunghezza', len(s))
        
