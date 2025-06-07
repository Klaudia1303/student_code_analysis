#Scrivere un programma che prende in ingresso un anno e verifica se
#esso è un anno bisestile, stampando a video i messaggi “anno bisestile”
#o “anno non bisestile”.
a=int(input("Inserisce un anno:"))
if a!=0 and a%4==0 and a%100!=0 or (a!=0 and a%4==0 and a%100==0 and a%400==0):
    print ("è un anno bisestile")
else:
    print("anno non bisestile")
