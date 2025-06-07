s=input('inserisci una stringa palindroma: ')
while s!=s[::-1]:
    print('la stringa',s,'non è palindroma')
    s=input('inserisci una stringa palindroma: ')
print('stringa palindroma di lunghezza',len(s))
