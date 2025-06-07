#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.7

stringa = input("Inserire una stringa: ");
count = 0;
i = 0;
while i < len(stringa):
    if stringa.count(stringa[i]) >= count:
        count = stringa.count(stringa[i]);
        pos = i;
    i += 1;
print(stringa[pos]);