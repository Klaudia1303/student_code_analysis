s=input('inserisci stringa con almeno un carattere ')
i=True
n=0
while i==True:
    while n<len(s) and i==True:
        if int(ord(str(s[n])))>100:
            print('il primo carattere con codice maggiore di 100 è: '+s[n])
            i=False
        else:
            n+=1
    if n>=len(s):
        print('stringa consumata e carattere non trovato')
        i=False
   
    
