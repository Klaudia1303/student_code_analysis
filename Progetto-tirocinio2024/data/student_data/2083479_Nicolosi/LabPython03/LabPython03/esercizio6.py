s=input('Inserisci una stringa: ')
n=0
while n<len(s) and ord(s[n])<100:
    n+=1
if n==len(s):
    print('Stringa consumata e carattere non trovato')
else:
    print('Il primo carattere con codice Unicode maggiore di 100 è',s[n])