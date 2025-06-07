#Scrivere un programma che prende in ingresso un anno e verifica se esso è un anno bisestile, stampando a
#video i messaggi “anno bisestile” o “anno non bisestile”.
a = int(input("inserisci un anno :"))
if a%4==0 and a%100 >=1 or a%400==0 :
    print ("è un anno bisestile")
else :
    print ("anno non bisestile")
