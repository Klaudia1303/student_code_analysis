#Scrivere un programma che prende in ingresso un anno e verifica se esso è un anno bisestile, stampando a
#video i messaggi “anno bisestile” o “anno non bisestile”.Nota: Un anno è bisestile se e solo se è divisibile per 4 ma non per 100, oppure è divisibile per 400.

x=int(input('inserisci un anno: '))

if (x%400==0 or x%4==0 and x%100!=0):
      print("l'anno è bisestile")
else:
    print("l'anno non è bisestile")
