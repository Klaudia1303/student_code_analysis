#Scrivere un programma che prende in ingresso un anno e verifica se esso è un anno bisestile, stampando a
#video i messaggi “anno bisestile” o “anno non bisestile”.
anno=int(input("Inserisci un anno: "));
if(anno%4==0):
    print("Anno Bisestile");
else:
    print("anno non bisestile");
