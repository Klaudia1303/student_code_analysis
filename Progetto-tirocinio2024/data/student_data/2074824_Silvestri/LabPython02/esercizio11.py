#11) Scrivere un programma che prende in ingresso un intero rappresentante una temperatura e stampa un
#messaggio sulla base della seguente tabella

t=input('inserisci temperaura: ')
t=int(t)
if 30<t:
    print('molto caldo')
elif 20<t<=30:
    print('caldo')
elif 10<t<=20:
    print('gradevole')
elif 1<=10:
    print('freddo')
