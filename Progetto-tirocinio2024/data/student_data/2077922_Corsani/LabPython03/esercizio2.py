#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.2

num = 0;

while int(num) <= 0:
    print("Inserisci un numero maggiore di zero: ",end="");
    num = input();
    if int(num) <=0:
        print("Numero non valido. Riprovare");

app = 0;
for app in range(int(num)+1):
    if int(app) >= 1:
        if int(num)%int(app) == 0:
            print(app);
    app = int(app) + 1;