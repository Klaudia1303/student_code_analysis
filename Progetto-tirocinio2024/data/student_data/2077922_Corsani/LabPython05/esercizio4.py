#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.4

n1 = input("Inserire il primo numero: ");
n2 = input("Inserire il secondo numero: ");

ris = 0

for i in range(1, int(n2)):
    while int(ris) < int(n2):
        ris = int(n1)*int(i);
        i += 1;
        if int(ris) < int(n2):
            print(ris);