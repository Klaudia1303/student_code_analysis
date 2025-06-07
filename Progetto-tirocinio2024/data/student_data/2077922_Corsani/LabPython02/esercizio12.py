#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.12

temp = input("Inserisci la temperatura: ",end="")
int(temp);
unit = input("Inserisci C se celcius o F se Fahrenheit: ",end="");
if unit != "C" and unit !="F":
    print ("Carattere non valido");

if unit == "C":
    if temp <= 0:
        print("Solida");
    elif temp > 0 and temp < 100:
        print("liquida");
    elif temp >= 100:
        print("Gassosa");

elif  unit == "F":
    temp = ((temp-32)/1.8);
    if temp <= 0:
        print("Solida");
    elif temp > 0 and temp < 100:
        print("liquida");
    elif temp >= 100:
        print("Gassosa");