stop =False
while noit stop:
    s=str(input('inserisci una stringa: '))
    i=0
    while i<len(s):
        x=s[i]
        i=i+1
        if ord(x)>100:
            prin('primo carattere con codice unicode maggiore di 100 è x')
            stop=True
        else:
            print('carattere non trovato')
        stop=True
