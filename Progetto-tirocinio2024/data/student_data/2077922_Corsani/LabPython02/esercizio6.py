#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.6

print("Inserisci il numeratore: ",end="");
numeratore = input();

print("Inserisci il denominatore: ",end="");
denominatore = input();

if int(numeratore) < int(denominatore):
    print("Frazione propria");
elif int(numeratore)%int(denominatore) == 0:
    print("Frazione apparente");
elif int(numeratore) > int(denominatore) and int(numeratore)%int(denominatore) != 0:
    print("Frazione impropria");