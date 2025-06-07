i = 0
while i>=0:
    s = input('inserisci una stringa palindroma: ')
    if s[ : ]== s[ : :-1]:
        print('stringa palindroma di lunghezza:', len(s))
        break
    else:
        print('stringa non palindroma')
    i+=1
