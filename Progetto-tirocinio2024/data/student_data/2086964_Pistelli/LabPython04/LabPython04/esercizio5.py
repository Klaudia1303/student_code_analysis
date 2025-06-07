import math
a=int(input('scivere un numero maggiore 0 uguale a 0 '))
if a<0:
    print('errore')
elif a==0 or a==1:
    print(1)
elif a>0 and a!=1:
    print(math.factorial(a))
