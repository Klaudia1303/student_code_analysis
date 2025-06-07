x=input('inserire stringa 1: ')
y=input('inserire stringa 2: ')
somma=' '
if len(x)==len(y):
    for i in range(0,len(x)):
        somma=somma+x[i]
        somma=somma+y[i]
    print(somma)
else:
    print('errore, stringhe non lunghe uguali')
