#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.4

num1 = int(-7);
num2 = int(-7);

app2 = 0;

while int(num1) < 0 or int(num1) > 10 and int(app2) < 2:
    print("Inserisci un numero compreso tra 0 e 10: ",end="");
    num1 = input();
    if int(num1) < 0 and int(num1) > 10:
        print("Numero non valido. Riprovare");
    app2 = int(app2)+1;

while int(num2) < 0 or int(num2) > 10 and int(app2) < 2:
    print("Inserisci un numero compreso tra 0 e 10: ",end="");
    num2 = input();
    if int(num2) < 0 and int(num2) > 10:
        print("Numero non valido. Riprovare");
    app2 = int(app2)+1;

for app in range(11):
    if int(app) != int(num1) and int(app) != int(num2):
            print(app);
    app = int(app) + 1;