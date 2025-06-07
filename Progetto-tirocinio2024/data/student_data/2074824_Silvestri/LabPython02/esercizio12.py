#12) Scrivere un programma che:
# a. chiede all’utente di inserire in input nell’ordine un valore che rappresenta una temperatura ed un
#carattere tra ‘F’ e ‘C’, rappresentante la scala utilizzata per la temperatura (C= Celsius, F=
#Fahrenheit).
# b. Stampa a video lo stato dell’acqua alla temperatura indicata tra “solida”, “liquida” o “gassosa”.
#Nota: Si ricorda che l’acqua è solida quando la temperatura è minore o uguale a 0 ◦ C ed è gassosa se la
#temperatura è maggiore o uguale a 100 ◦ C.
#La formula per convertire la temperatura tra Celsius e Fahrenheit è: C = (F − 32)/1.8, dove C indica la
#temperatura in gradi Celsius e F indica la temperatura in gradi Fahrenheit.

var1=input('inserire temperatura: ')
var2=input('inserire se celsius "C" o fahrenheit "F": ')
var1=int(var1)

if var2==C:
    if var1<=0:
        print('solida')
    elif 0<var1<100:
        print('liquida')
    elif 100<=var1:
        print('gassosa')
elif var2==F:
    if var1<=32:
        print('solida')
    elif 32<var1<((100*1,8)+32):
        print('liquida')
    elif ((100*1,8)+32)<=var1:
        print('gassosa')
