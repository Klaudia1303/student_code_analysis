i=True
c=0

while i:
    n=input('inserisci un intero(* per terminare): ')
    if n!='*':
        if int(n)<0:
            c=c+int(n)
    else:
        i=False

print(c)
