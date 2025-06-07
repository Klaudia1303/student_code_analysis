vero=True
totale=0
while vero:
    s=input('inserisci una stringa:')
    if s.count('a')>0 and s.count('c')>0:
        vero=False
    totale+=1
print('Il totale dlle stringhe inserite è:',int(totale))
