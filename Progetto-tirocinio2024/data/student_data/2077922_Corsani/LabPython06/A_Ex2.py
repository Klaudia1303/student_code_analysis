#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.2

stringa = input("Inserire una stringa: ");

lunghezza = len(stringa);

livello = "Non palindroma";

for i in range(0, lunghezza):
    if i == 0:
        if stringa[i] == stringa[lunghezza-(i+1)]:
            livello = i+1;
        else:
            print(livello);
            break;
        
    if i > 0:
        if stringa[i] == stringa[lunghezza-(i+1)]:
            livello = livello+1;
        else:
            print("Livello", livello);
            break;

print("Livello", lunghezza, "Palindroma di livello massimo");