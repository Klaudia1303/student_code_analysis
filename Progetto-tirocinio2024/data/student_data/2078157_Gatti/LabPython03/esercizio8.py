s = input('inserisci una stringa palindroma: ')
b = True
while b:
    if s[:] == s[::-1]:
        print('stringa palindroma di lunghezza: ', len(s))
        b = False
    else:
        s = input('inserisci una stringa palindroma: ')


