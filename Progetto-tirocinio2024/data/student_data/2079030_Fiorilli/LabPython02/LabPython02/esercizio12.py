t=float(input('inserisci il valore della temperatura: '))
s=input('inserisci un simbolo tra "F" e "C": ')
if s=='F' or s=='f':
    t=(t-32)/1.8
if t>=100:
    print ('gassosa')
elif t>0:
    print ('liquida')
else:
    print ('solida')
