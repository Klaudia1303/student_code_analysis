#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.2

s = input("Inserire una stringa: ");
n = input("Inserire un numero intero positivo: ");

lun = len(s);

for i in range(0, lun):
    aggiunta = s[i];
    if i < 1:
        for n in range(0, int(n)):
            stringa = aggiunta;
            stringa +=aggiunta;
            n += 1;
    else:
        for n in range(0, int(n)):
            stringa +=aggiunta;
            n += 1;
        #stringa = stringa + aggiunta;
    i += 1;

print(stringa);