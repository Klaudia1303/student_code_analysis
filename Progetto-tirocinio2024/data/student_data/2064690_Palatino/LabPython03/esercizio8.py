s=input('inserisci una stringa palindroma: ')
while s!=reversed(s):
    print('stringa non palindroma')
    s=input('inserisci una stringa palindroma: ')
print('stringa palindroma di lunghezza',len(s))

