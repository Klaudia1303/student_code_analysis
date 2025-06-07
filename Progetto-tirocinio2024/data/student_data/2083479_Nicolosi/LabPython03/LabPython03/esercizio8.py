s=input('Inserisci una stringa palindroma: ')
while str(s)!=str(s)[::-1]:
    s=input('Non palindroma, inserire una stringa palindroma: ')
if str(s)==str(s)[::-1]:
    print('Stringa palindroma di lunghezza',len(s)-1)