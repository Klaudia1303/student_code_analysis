#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.8

palindroma = False;

while palindroma == False:
    print("Inserisci una parola: ",end="");
    stringa = input();

    if str(stringa) == str(stringa)[::-1]:
        print("Stringa palindroma di lunghezza", len(stringa));
        palindroma = True;
    else:
        print("Non palindroma.");