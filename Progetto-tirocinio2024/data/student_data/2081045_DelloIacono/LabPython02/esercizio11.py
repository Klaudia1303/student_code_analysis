temperatura=int(input('inserire numero intero: '))
if (30<temperatura):
    print('molto caldo')
elif (20<temperatura<=30):
    print('caldo')
elif (10<temperatura<=20):
    print('gradevole')
elif (temperatura<=10):
    print('freddo')
