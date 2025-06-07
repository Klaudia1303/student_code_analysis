n=input('inserisci un valore intero (* per terminare): ')
c=0
while n!='*':
    if int(n)>=0:
        c+=1
    n=input('inserisci un valore intero (* per terminare): ')
print (c)
