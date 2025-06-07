x=input("Scrivere 'F' per temperatura in scala Fahrenheit o 'C' per temperatura in scala Celsius: ")
t=int(input('temperatura: '))
if(x=='C' or x=='c' and t>=100) or (x=='F' or x=='f' and t>=132/1.8):
      print('gassosa')
elif (x=='C' or x=='c' and t<=0) or (x=='F' or x=='f' and t<=32/1.8):
    print('solida')
elif (x=='C' or x=='c' and 0<t<100) or (x=='F' or x=='f' and 32/1.8<t<132/1.8):
    print('liquida')
