t=float(input('inserisci i dati di ingresso'))
s=input('inserisci i dati di ingresso')
if s.upper()=='F':
    t=(t-32/1.8)
if t<=0:
    print('solida')
elif t>=100:
    print ('gassosa')
elif t>0 and t<100:
    print('liquida')
