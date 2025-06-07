#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.8

print("Inserici il primo lato: ",end="");
lato1 = input();

print("Inserici il secondo lato: ",end="");
lato2 = input();

print("Inserici il terzo lato: ",end="");
lato3 = input();

if lato1 > 0 and lato2 > 0 and lato3 > 0 and lato1 < (lato2+lato3) and lato2 < (lato1+lato3) and lato3 < (lato2 + lato1):
 print("Triangolo valido");
else:
    print("Triangolo non valido");

if (lato1 == lato2) and (lato2 == lato3) and (lato3 == lato1):
    print("Il triangolo è equilatero");
elif (lato1 == lato2) or (lato2 == lato3) and (lato3 == lato1):
    print("Il triangolo è isoscele");
else:
    print("Il triangolo è scaleno");