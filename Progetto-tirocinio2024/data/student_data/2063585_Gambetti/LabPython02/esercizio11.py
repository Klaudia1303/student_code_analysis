t=int(input('inserisci una temperatura: '))
if int(t)<=10:
    print('freddo')
elif int(t)>10 and int(t)<=20:
    print('gradevole')
elif int(t)>20 and int(t)<=30:
    print('caldo')
elif int(t)>30:
    print('molto caldo')
