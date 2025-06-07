corretto=False
s=input('Inserire stringa palindroma: ')
while not corretto:
    if s==s[::-1]:
        print('stringa palindroma di lunghezza',len(s))
        corretto=True
    else:
        print('non palindroma, inserire una stringa palindroma')
        s=input('Inserire stringa palindroma: ')
