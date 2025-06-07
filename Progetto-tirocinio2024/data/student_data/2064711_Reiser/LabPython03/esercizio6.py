s= input('inserire una stringa: ')

c=True
n= 0

while c==True:
    while n<len(s) and c==True:
        if int(ord(str(s[n])))>100:
            print("Il primo carattere con codice Unicode maggiore di 100 è: "+s[n])
            c=False
        else:
            n=n+1
    if n>=len(s):
        print('stringa consumata e carattere non trovato')
        c=False
    else:
        ''
