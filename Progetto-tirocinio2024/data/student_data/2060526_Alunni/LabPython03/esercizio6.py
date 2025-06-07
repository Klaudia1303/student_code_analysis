n=(input('inserisci una sringa valida: '))
l=int(len(n)-1)
x=0
N=ord(n[x])
while x<l and not N>100:
    x=x+1
    N=ord(n[x])

if(N>100):
    print('Il primo carattere con codice Unicode maggiore di 100 è '+ n[x])
else:
    print('stringa consumata e carattere non trovato')
