t = float(input('Inserire il valore della temperatura:'))
scala = input('Inserire un carattere tra \'F\' e \'C\':')

scala == 'F' or 'C'

# C = ( F - 32.0 ) / 1.8
# F = ( C * 1.8 ) + 32

if scala == 'C' and t <= 0.0:
    print('solida')
elif scala == 'C' and 0.0<t<100.0:
    print('liquida')
elif scala == 'C' and t>=100.0:
    print('gassosa')



if scala == 'F' and t<=32.0:
    print('solida')
elif scala == 'F' and 32.0<t<212.0:
    print('liquida')
elif scala == 'F' and t>= 212.0:
    print('gassosa')

