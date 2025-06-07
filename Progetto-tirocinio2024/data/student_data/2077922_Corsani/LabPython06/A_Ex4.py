#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.4

a = 0;
b = 0;

for i in range(1,1000):
    a = a + 20;
    b = b + i;

    if a <= b:
        print("Il secondo viaggiatore ha impiegato", i,"giorni a raggiungere il primo.");
        break;