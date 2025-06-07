palindroma=False

while not palindroma:
    s=input('inserisci una stringa palindroma: ')
    if s[-1]==s[0]:
        palindroma=True
    else:
        print('Frase non palindroma, inserire una nuova stringa palindroma')
print('Stringa palindroma di lunghezza', len(s))
