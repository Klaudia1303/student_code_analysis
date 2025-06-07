t=int(input('Inserisci la temperatura '))
if(t>30):
    print('molto caldo')
elif(t<=30 and t>20):
    print('caldo')
elif(t<=20 and t>10):
    print('gradevole')
elif(t<=10):
    print('freddo')
