s=str(input('inserisci una stringa: '))
c=0
n=int(ord(s[c]))
if n>100 :
    print('Il primo carattere con codice Unicode maggiore di 100 è ', s[c])
while n<=100 :
    c=c+1
    if c>=len(s):
        print('stringa consumata e carattere non trovato')
        n=200
    else:
        n=int(ord(s[c]))
        if n>100:
            print('Il primo carattere con codice Unicode maggiore di 100 è ', s[c])
