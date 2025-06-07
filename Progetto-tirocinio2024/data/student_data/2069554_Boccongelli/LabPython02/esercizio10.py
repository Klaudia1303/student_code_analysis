e = float(input('Inserisci età del cane: '))

if (e >= 0):
    if (e >= 2):
        print('Età umana: ' + str(((e - 2) * 4) + 21) + ' anni')
    else:
        print('Età umana: ' + str(e * 10.5) + ' anni')
    
        
