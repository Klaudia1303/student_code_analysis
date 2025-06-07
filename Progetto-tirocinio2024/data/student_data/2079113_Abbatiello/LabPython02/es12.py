inp = input()
inp = inp.strip()
inp = inp.upper()


pos = (inp.rfind('F' or 'C'))

t = (inp.replace('F' , '' ,pos)) or (inp.replace('C' , '' , pos))

t = float(t)

if 'F' in inp:
    print('Fahrenheit')
    if t <= 32:
        print('solida')
    elif t >= 212:
        print('gassosa')
    else:
        print('liquida')

if 'C'in inp:
    print('Celsius')
    if t <= 0:
        print('solida')
    elif t >= 100:
        print('gassosa')
    else:
        print('liquida')
