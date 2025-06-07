temp=float(input('Inserire temperatura: '))
scala=input('Inserire scala in maiuscolo: ')
if scala=='F':
    temp=(temp-32)/1.8
if temp<=0:
  print('solida')
elif temp>0 and temp<=100:
    print('liquida')
elif temp>100:
    print('gassosa')
