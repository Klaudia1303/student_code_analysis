s=input('Inserisci una stringa: ')
i=0
l=1
while i<len(s): #i<len(s) significa che la stringa non è costituita
                #da alcun carattere
    if ord(s[i])>100:
        print('Il primo carattere UNICODE maggiore di 100 è: ',s[i])
        l=1
        i=len(s)
    else:
        l=2
    i+=1

if l!=1:
    print('Stringa consumata e carattere non trovato')
