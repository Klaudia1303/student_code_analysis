#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.9

print("Inserisci l'anno: ",end="")
anno = input();

print("Inserisci il mese: ",end="")
mese = input();

if int(mese) > 12:
    print("Errore di inserimento mese");

if int(mese) == 12:
    print(1, int(anno) + 1);
else:
    print(int(mese)+1, anno);