S = input('inserisci una stringa')
i=0

if len(S)>0:
    check=True
    while i<len(S)and check==True:
        if ord(S[i])>100:
            print('la stringa si è interrotta perchè non è stato trovato il carattere' ,S[i])
            check==False
        i+=1
elif check==True:
    print('la stringa è terminata')
