n=int(input('inserire una temperatura: '))
scala=str(input('inserire il primo carattere della scala utilizzata: (C oppure F) '))
if (scala=='F'):
    n=(float(n)-32)/1,8
if (n<=100 and n>=0):
       print('liquida')
elif (n<0):
    print('solida')
else:
    print('gassosa')
