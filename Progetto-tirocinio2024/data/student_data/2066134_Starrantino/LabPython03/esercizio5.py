while True:
    s = input('> ')
    print(s[0], s[-1], sep='')
    if s.islower() and s.isalpha():
        break