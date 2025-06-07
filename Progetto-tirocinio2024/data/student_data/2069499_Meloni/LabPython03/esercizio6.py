s=input('Inserisci la stringa ')
i=0
while(i<=(len(s)-1)):
    if(ord(s[i])<=100):
        i+=1
    else:
         print('Il primo carattere Unicode maggiore di 100 è ', s[i])
         i=len(s)+1
if(i==len(s)):
        print('stringa consumata e carattere non trovato')
