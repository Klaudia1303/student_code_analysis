#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.8

test = True;
count = 0;

while test:
    stringa = input("Inserire una stringa: ");

    posto = len(stringa);

    if count > 0:
        primalettera = stringa[0:1];
        if primalettera == ultimalettera:
            test = False;
        else:
            ultimastringa = stringa;
            ultimalettera = ultimastringa[int(posto)-1 : int(posto)];
    else:
        ultimastringa = stringa;
        ultimalettera = ultimastringa[int(posto)-1 : int(posto)];
        count = count +1;

print(ultimastringa, stringa);