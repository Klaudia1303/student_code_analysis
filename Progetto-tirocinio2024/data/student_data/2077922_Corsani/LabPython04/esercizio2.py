#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.2

test = True;
count = 0;

while test:
    num = input("Inserire un numero. Scrivere * per terminare. Numero: ");
    if num == "*":
        test = False;
    elif int(num) > 0:
        count = count + 1;
    

print(count);