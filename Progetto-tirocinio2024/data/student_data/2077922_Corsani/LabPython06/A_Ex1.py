#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.1

test = True;

while test:
    num1 = int(input("Inserire il primo numero maggiore di 0: "));
    num2 = int(input("Inserire il secondo numero maggiore di 0: "));

    if num1 > 0 and num2 > 0:
        test = False;
    else:
        print("Numeri non validi. Riprovare.");

if num1 > num2:
    numero = num1;
else:
    numero = num2;

for i in range (1, numero+1):
    if num1%i == 0 and num2%i != 0:
        print(i);
    i += 1;