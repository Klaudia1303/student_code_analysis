#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.1

test = True;

while test:
    str1 = input("Inserire la prima stringa: ");
    str2 = input("Inserire la seconda stringa: ");

    if len(str1) != len(str2):
        print("Le lunghezze delle stringhe non corrispondono. Riprovare.");
    else:
        test = False;

lun = len(str1);

for i in range (0, lun):
    aggiunta = str1[i] + str2[i];
    if i < 1:
        stringa = aggiunta;
    else:
        stringa = stringa + aggiunta;
    i += 1;

print(stringa);