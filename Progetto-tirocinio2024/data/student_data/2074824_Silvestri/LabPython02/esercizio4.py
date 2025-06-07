#Scrivere un programma che prende in ingresso una stringa s non vuota e verifica se il primo e l’ultimo
#carattere sono uguali. In caso positivo stampa “caratteri iniziale e finale uguali” altrimenti stampa “caratteri
#iniziale e finale diversi”. Ad esempio, se s=“ambasciata” il programma deve stampare “caratteri iniziale e
#finale uguali”.
s=input("Inserisci una parola:")
s[0]
s[len(s)-1]
if (s[0]==s[len(s)-1]):
  print ("Caratteri iniziale e finale uguali")
else:
  print ("Caratteri iniziale e finale diversi")
