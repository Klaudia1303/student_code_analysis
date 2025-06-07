t=input('inserire la temperatura: ')
t=float(t)
scala=input('inserire F o C: ')
sca=ord(scala)
if sca==ord('F') or sca==ord('f'):
    C=(t-32)/1.8
    if C<=0:
        print('solida')
    elif C>=0:
        print('gassosa')
    else:
        print('liquido')
if sca==ord('C') or sca==ord('c'):
    if t<=0:
        print('solida')
    elif t>=0:
        print('gassosa')
    else:
        print('liquido')
