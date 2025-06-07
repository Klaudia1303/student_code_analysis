t=int(input('Inserire una temperatura: '))
c=(input('Inserire F per Fahrenheit e C per Celsius: '))
if c!='c' and c!='f'and c!='C' and c!='F':
   print('Input non valido')
else:
    if c=='F' or c=='f':
       t=(t-32)/1.8
if t<=0:
   print('Solida')
elif 0<t<100:
   print('Liquida')
else:
   print('Gassosa')
