#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.10

print("Inserisci l'età del cane: ",end="");
cane = input();

if float(cane) < 0:
    print("L'età del cane non può essere minore di 0")
else:
    if float(cane) <= 2:
        eta = 10.5*float(cane);
        print("L'età del cane in età umana è:", eta);
    else:
        eta = (10.5*2)+((float(cane)-2)*4)
        print("L'età del cane in età umana è:", eta);