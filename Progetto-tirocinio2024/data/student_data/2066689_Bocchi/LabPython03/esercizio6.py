s= input('stringa: ')
len(s)
x= 0
trovata = False

while x<len(s):
    s[x]
    a = ord(s[x])
    if a > 100:
       print('il primo carattere con codice Unicode maggiore di 100 è', s[x])
       trovata = True
       x = len(s)
    x=x+1
    
if trovata == False:
    print('stringa consumata senza trovare il carattere')
