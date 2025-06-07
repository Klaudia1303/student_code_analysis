corretto=False
while not corretto:
    s=input('Inserie una stringa: ')
    sp=s[::-1]
    if(s==sp):
        print('Stringa palindroma di lunghezza:',len(s))
        corretto=True
    else:
        print('Stringa non palindroma')
        
