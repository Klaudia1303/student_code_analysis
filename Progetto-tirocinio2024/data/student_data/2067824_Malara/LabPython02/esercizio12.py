valoreT=float(input('temperatura '))
scalaT=input('scrivere in maiuscolo riferimento scala, C/F ')
T=valoreT,scalaT
if scalaT=='F':
    convertFinC=(valoreT-32)/1.8
else:
    convertFinC=valoreT
if convertFinC<=0:
    print('solida')
elif convertFinC>100:
    print('gassosa')
else:
    print('liquida')

    

