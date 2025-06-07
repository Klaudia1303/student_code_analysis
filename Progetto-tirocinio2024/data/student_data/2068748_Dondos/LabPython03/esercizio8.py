palindroma=False

while not palindroma:
    s=input('Inserisci una stringa palindroma: ')
    if s[::-1]==s[0:]:
        palindroma=True
    else:
        print('non palindroma, inserire una stringa palindroma')
print('stringa palindroma di lunghezza', len(s))
