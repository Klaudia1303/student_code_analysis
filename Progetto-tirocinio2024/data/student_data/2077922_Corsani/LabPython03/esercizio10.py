#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.10

num = 0;

while int(num) <= 1:
    print("Inserisci un numero maggiore di uno: ",end="");
    num = input();
    if int(num) <= 1:
        print("Numero non valido. Riprovare");

app = 1;
while app <= int(num):
    numprimo = True;
    divisore = 2;
    while int(divisore) <= int(app):
        if int(app)%int(divisore) == 0:
            numprimo = False;
        divisore = divisore + 1;
    if numprimo == True:
        print(app);
    app = app +1;