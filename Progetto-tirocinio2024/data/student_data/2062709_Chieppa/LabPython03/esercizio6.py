s=input('inserire stringa: ')
x=0
check=True
while x<len(s) and check==True:
    if ord(s[x])>100:
        print('Il primo carattere con codice Unicode maggiore di 100 è',s[x])
        check=False
    x+=1
if check==True:
    print('stringa consumata e carattere non trovato')
