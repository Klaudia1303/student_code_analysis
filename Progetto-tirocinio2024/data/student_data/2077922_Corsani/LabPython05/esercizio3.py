#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.3

str1 = input("Inserire la prima stringa: ");
str2 = input("Inserire la seconda stringa: ");

for i in range(len(str1)):
    if str1[i] not in str2:
        print(str1[i],end="")