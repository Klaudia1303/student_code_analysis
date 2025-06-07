i=True
while i:
    s=input('stringa=')
    if s==s[::-1]:
        print('stringa palindroma di lunghezza',len(s))
        i=False
    else:
        print('non palindroma, inserire una stringa palindroma: ')
