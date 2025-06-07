temp = float(input('Inserisci una temperatura: '))
typ = input('Inserisci una scala ("F" p "C"): ')

if (typ == 'C' or typ == 'F'):
    if (typ == 'F'):
        temp = (temp - 32)/1.8
    if (temp >= 100):
        print('gassosa')
    elif (temp >= 0):
        print('liquida')
    else:
        prin('solida')
