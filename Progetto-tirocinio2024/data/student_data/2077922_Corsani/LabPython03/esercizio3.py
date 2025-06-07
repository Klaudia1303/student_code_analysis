#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.3

app = 0;

while int(app) <= 0:
    print("Inserisci un numero: ",end="");
    num = input();

    if int(num)%5 == 0:
        app = 1;
    else:
        print("Numero non divisibile per 5");

print(num);

