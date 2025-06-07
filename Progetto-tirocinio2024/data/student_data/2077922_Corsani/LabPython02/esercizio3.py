#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.3

import math

print("Inserisci la stringa: ",end="");
stringa = input();

print("Inserisci un numero: ",end="");
numero = input();

if int(numero)%2 == 0:
    print("Numero pari.")
else:
    print("Numero dispari. La tua stringa è:", stringa);