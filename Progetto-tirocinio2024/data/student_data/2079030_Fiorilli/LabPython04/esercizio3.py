n=input('inserisci un valore intero (* per terminare): ')
s=0
while n!='*':
    if int(n)<0:
        s=s+int(n)
    n=input('inserisci un valore intero (* per terminare): ')
print (s)
