#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.1

test = True;
count = 0;

while test:
    stringa = input("Inserire una stringa. Quando si inserirà una stringa contenente i caratteri C ed A, il programma terminerà. Stringa: ");
    
    count = count + 1;

    test2 = stringa.find("c");
    test3 = stringa.find("a");

    if int(test2) != -1 and int(test3) != -1:
        test = False;

print(count);