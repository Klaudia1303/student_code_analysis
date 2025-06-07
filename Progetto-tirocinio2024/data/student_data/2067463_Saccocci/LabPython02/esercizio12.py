t=float(input('Inserire un valore per la temperatura:'))
g=input('Inserire il carattere rappresentante la scala utilizzata,"F" o "C":')
tC=(t-32)/1.8
if g=='C':
    if t<=0:
        print('L\'acqua è allo stato solido')
    elif 0<t<100:
        print('L\'acqua è allo stato liquido')
    elif t>=100:
        print('L\'acqua è allo stato gassoso')
elif g=='F':
    if tC<=0:
        print('L\'acqua è allo stato solido')
    elif 0<tC<100:
        print('L\'acqua è allo stato liquido')
    elif tC>=100:
        print('L\'acqua è allo stato gassoso')
else:
    print('Il carattere inserito non è valido')
