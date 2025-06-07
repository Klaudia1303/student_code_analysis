#Scrivere un programma che prende in ingresso una stringa s non vuota e verifica se il primo e l’ultimo
#carattere sono uguali. In caso positivo stampa “caratteri iniziale e finale uguali” altrimenti stampa “caratteri
#iniziale e finale diversi”. Ad esempio, se s=“ambasciata” il programma deve stampare “caratteri iniziale e
#finale uguali”.

s=input('inserisci una stringa: ')

x=(s[0:1])
y=(s[-1:])

if x==y :
   print('caratteri iniziale e finale uguale')
else:
    print('caratteri iniziale e finale diverso')
