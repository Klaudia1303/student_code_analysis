#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.9

test = True;

while test:
    lato = input("Inserire il lato del quadrato (numero dispari, maggiore o uguale a 3): ");

    if int(lato)%2 == 0:
        print("Il lato deve essere un numero maggiore o uguale a 3 e dispari. Riprovare.");
    else:
        test = False;

for i in range(0, int(lato)):
    if i < int(lato)-1 and i > 0:
        j = 1;
        e = 0;
        while j < 3:
            print("*",end="");
            while e < int(lato):
                print(" ",end="");
                e += 2;
            j += 1;

    if i == 0 or i == int(lato)-1:
        j = 1;
        while j < int(lato)+1:
            print("*",end="");
            j += 1;
    print("");