t=int(input('Inserire temperatura: '))
if(t>30):
    print('Molto caldo')
else:
    if(t>20 and t<=30):
        print('Caldo')
    else:
        if(t>10 and t<=20):
            print('Gradevole')
        else:
            print('Freddo')
