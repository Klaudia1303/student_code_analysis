c=True
while c:
    s=str(input('Stringa '))
    if s!="":
        c=False

i=0
while i<=len(s):
    if ord(s[i])>100:
        print('Il primo carattere con codice Unicode maggiore di 100 Ã¨ '+s[i])
        i=len(s)+1
    else:
        i=i+1
    if i==len(s):
        print('Stringa consumata e carattere non trovato ')
