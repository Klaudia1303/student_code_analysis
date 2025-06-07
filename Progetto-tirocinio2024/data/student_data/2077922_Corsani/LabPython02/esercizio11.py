#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.11

print("Inserisci la temperatura: ",end="");
temp = input();

if temp > 30:
    print("Molto caldo");
elif temp >= 20 and temp < 30:
    print("Caldo");
elif temp >= 10 and temp < 20:
    print("Gradevole");
elif temp <= 10:
    print("Freddo");
