corretto=False
while not corretto:
    s=input('inserire una stringa palindroma')
    if str(s)==str(s)[::-1]:
        print('stringa palindroma di lunghezza', len(s))
        corretto:True
    else:
        print('non palindroma')
