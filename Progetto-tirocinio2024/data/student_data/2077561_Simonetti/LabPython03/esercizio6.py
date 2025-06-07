s=input('type a word: ')
i=0
if len(s)==1 and ord(s)<=100:
    print('stringa di lunghezza 1 e codice UNICODE del carattere inferiore di 100.')
elif i<len(s):
    while i<len(s):
        print(s[i],end='\n')
        if ord(s[i])>100:
            print('Il primo carattere con codice UNICODE maggiore di 100 è:',s[i])
            break
        i+=1
if ord(s[i-1])<100:
    print('stringa consumata e carattere non trovato.')
    
