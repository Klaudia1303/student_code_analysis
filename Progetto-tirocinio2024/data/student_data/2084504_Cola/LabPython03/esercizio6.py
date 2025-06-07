s=input('scrivere una frase: ')
i=0
x=ord(s[i])
while (not (s[i]==s[-1])) and (x<=100):
    i=i+1
    x=ord(s[i])
if x>100:
    print('Il primo carattere con codice Unicode maggiore di 100 è',s[i])
else:
    print('stringa consumata e carattere non trovato')
