corretto=False
while not corretto:
    s=input('inserisci stringa palindroma:')
    if s==s[::-1]:
        print('stringa palindroma di lunghezza',len(s))
        corretto=True
    elif s!=s[::-1]:
        print('non palindroma, inserire una stringa palindroma: ')
    
    
    
