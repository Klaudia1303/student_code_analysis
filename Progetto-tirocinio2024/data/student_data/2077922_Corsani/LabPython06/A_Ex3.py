#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.3

for i in range(0, 8):
    for n in range(0,8):
        ris = n*i;
        if ris > 8:
            ris = ris+2;
        print(n, "x", i, ris);