#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.1

num = 0;

while int(num) <= 2:
    print("Inserisci un numero maggiore di due: ",end="");
    num = input();
    if int(num) <=2:
        print("Numero non valido. Riprovare");

app = 2;
for app in range(int(num)+1):
    if int(app) >= 2:
        if int(app)%2 == 0:
            print(app);
    app = int(app) + 1;
