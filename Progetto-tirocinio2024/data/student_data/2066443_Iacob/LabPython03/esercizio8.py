stop = False
while not stop:
    s = str(input('Insert palindrome word: '))
    if s[::]==s[::-1]:
        print('Stringa palindroma di lunghezza',len(s))
        stop = True
    else: print('Non palindroma')
