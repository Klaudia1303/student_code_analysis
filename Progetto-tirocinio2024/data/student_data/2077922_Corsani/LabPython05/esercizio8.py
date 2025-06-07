#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.8

test = True;

while test:
    base = input("Inserire la base del triangolo (numero dispari, maggiore o uguale a 3): ");

    if int(base)%2 == 0:
        print("La base deve essere un numero maggiore o uguale a 3 e dispari. Riprovare.");
    else:
        test = False;


print("*")

for i in range(0, int(base)):
    j = 1;
    if i%2 != 0:
        while j <= i+1:
            print("*",end="");
            j += 1;
        print(" ");