#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.4

test = True;
count = 0;

while test:
    num = input("Inserire un numero. Scrivere * per terminare. Numero: ");
    if int(num) == 0:
        test = False;
    elif int(num)%3 == 0:
        count = count + int(num);
    

print(count);