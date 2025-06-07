while True:
    s = input('> ')
    if s == s[::-1]:
        print('stringa palindroma di lunghezza', len(s))
        break
    print('non palindroma, inserire una stringa palindroma: ')