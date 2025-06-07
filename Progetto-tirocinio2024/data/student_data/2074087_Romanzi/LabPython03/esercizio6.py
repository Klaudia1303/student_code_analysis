c=True
while c:
    s=str(input('Stringa '))
    if s!="":
        c=False

p=0
while p<=len(s)-1:
    if ord(s[p])>100:
        print('Il primo carattere con codice Unicode maggiore di 100 è '+s[p])
        p=len(s)+1
    else:
        p=p+1
    if p==len(s):
        print('Stringa consumata e carattere non trovato ')
