s=input('Inserire una stringa: ')
i=0
corretto=False
while not corretto:
    n=ord(s[i])
    l=len(s)
    if(n>100):
        print('Il primo carattere con codice Unicode maggiore di 100 è',s[i])
        corretto=True
    else:
        if i==l-1:
            print('Stringa consumata e carattere non trovato')
            corretto=True
    i=i+1


        
    
    
