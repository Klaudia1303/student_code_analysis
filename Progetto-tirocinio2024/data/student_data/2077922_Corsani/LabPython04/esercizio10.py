#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.10

stringa1 = input("Inserire una stringa: ");
stringa2 = input("Inserire una stringa: ");
stringa3 = input("Inserire una stringa: ");
while len(stringa1)+len(stringa2)!=len(stringa3):
    stringa1 = stringa2;
    stringa2 = stringa3;
    stringa3 = input("Inserire una stringa: ");
print(stringa1,stringa2,stringa3);