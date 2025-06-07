#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.5

test = False;

while test == False:
    print("Inserisci una stringa. Per terminare, interisci una stringa composta esclusivamente da caratteri minuscoli: ",end="");
    stringa = input();

    ncaratteri = len(stringa);
    print(stringa[0]+stringa[-1]);

    test = stringa.islower();
    if stringa.isalpha() == False:
        test = False;
