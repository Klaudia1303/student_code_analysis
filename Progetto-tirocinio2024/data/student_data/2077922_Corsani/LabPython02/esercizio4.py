#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.4

print("Inserisci la stringa: ",end="");
stringa = input();

app = len(stringa);

if stringa[0] == stringa[app-1]:
    print("Caratteri iniziale e finale uguali");
else:
    print("Caratteri iniziale e finale diversi");