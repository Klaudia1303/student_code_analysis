corretto=True
while corretto:
    s=input('Inserisci una stringa palindroma: ')
    if str(s)==str(s)[::-1]:
        print('stringa palindroma di lunghezza',len(s))
        corretto=False
    else:
        print('stringa non palindroma,inserisci una stringa palindroma')
        stringa=input('Inserire una stringa palindroma: ')
