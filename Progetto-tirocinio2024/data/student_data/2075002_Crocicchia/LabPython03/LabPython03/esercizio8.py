finito=False
while not finito:
    s=input('inserire una stringa palindroma: ')
    if s==s[::-1]:
        print('stringa palindroma di lunghezza: ',len(s))
        finito=True
    else:
        print('non palindroma')
    