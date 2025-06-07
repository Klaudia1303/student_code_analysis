t=int(input('inserire un valore che rappresenta una temperatura:'))
x=input('inserire un carattere a scelta tra "F" e "C":')
y=(t-32)/1.8
if x=='C':
    if t<=0:
        print('solida')
    elif t>=100:
        print('gassosa')
    elif 0<t<100:
        print('liquida')
elif x=='F':
    if y<=0:
        print('solida')
    elif y>=100:
        print('gassosa')
    elif 0<y<100:
        print('liquida')
else:
    print('carattere inserito non valido')
