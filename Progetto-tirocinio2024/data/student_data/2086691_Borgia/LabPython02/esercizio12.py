scala=input('Inserire C per la scala Celsius oppure inserire F per la scala Fahrenheit ')
temp=float(input('Inserire la temperatura dell acqua '))
if scala=='c' and temp==0:
    print:('solida')
elif 0<temp<100:
    print('liquida')
else:
    print('gassosa')
if scala=='f' and temp==32:
    print:('solida')
elif 32<temp<212:
    print:('liquida')
else:
    print:('gassosa')
