#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.6

num1 = int(input("Inserisci il primo numero: "));
num2 = int(input("Inserisci il secondo numero: "));

count = 0;
risultato = 0;

while int(count) < num2:
    risultato = risultato + num1;
    count = count + 1;

print(risultato);