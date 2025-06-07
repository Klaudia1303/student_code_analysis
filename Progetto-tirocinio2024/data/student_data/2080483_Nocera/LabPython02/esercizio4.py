#Scrivere un prograambiamma che prende in ingresso una stringa s non vuota e verifica se il primo e l’ultimo
#carattere sono uguali. In caso positivo stampa “caratteri iniziale e finale uguali” altrimenti stampa “caratteri
#iniziale e finale diversi”. Ad esempio, se s=“ambasciata” il programma deve stampare “caratteri iniziale e
#finale uguali”.
s = str(input("scrivere una parola :"))
if s[0] == s[-1]:
        print ("caratteri iniziale e finale uguali :")
else : print ("caratteri iniziale e finale diversi")


