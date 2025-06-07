#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.7


print("Inserisci il 1° numero: ",end="")
x = input();

print("Inserisci il 2° numero: ",end="")
y = input();

print("Inserisci il 3° numero: ",end="")
z = input();

vet = [x, y, z];

vet.sort();

print(vet);