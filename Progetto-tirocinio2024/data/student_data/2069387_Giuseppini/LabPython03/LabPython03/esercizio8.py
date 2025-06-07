i=True
s=input('inserisci una stringa: ')
while i:
    if s[0:]==s[::-1]:
        print('stringa palindroma di lunghezza', len(s))
        i=False
    else:
        s=input('non palindroma, inserire una stringa palindroma: ')
