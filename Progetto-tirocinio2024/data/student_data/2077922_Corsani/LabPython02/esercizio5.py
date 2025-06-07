#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.5

import math;

print("Inserisci l'anno: ",end="")
anno = input();

if int(anno)%4 == 0 and int(anno)%100 != 0:
    print("L'anno",anno,"è bisestile");
elif int(anno)%400 == 0:
    print("L'anno",anno,"è bisestile");
else:
    print("L'anno",anno,"non è bisestile");
