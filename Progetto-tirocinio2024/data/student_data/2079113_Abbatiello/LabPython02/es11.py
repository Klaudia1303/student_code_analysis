t = int(input('inserisci temperatura :'))
if 30 < t:
    print('molto caldo')
elif t > 20 and t <= 30 :
    print('caldo')
elif t > 10 and t <= 20:
    print('gradevole')
elif t <=10 :
    print('freddo')
