temp=float(input('inserire temperatura '))
scala=input('inserire scala ("C" o "F"): ')
if(scala=='F'):
    temp=((temp-32)/1.8)
    scala='C'
if(scala=='C'):    
    if(temp<=0):
        print('solida')
    if(0<temp<100):
        print('liquida')
    if(100<=temp):
        print('gassosa')
else:
        print('scala sbagliata')