s=input('inserisci una parola palindroma: ')
finito=False
while not finito:
    if s[::-1]!=s:
        print('non palindroma')
        s=input('inserire una stringa palindroma: ')
    else:
        l=len(s)
        print('stringa palindroma di lunghezza', l)
        finito=True


