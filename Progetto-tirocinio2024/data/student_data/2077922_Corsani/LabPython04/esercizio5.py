#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.5

test = True
while test:
    num = int(input('Inserire un numero: '))
    if int(num) >= 0:
        test = False;
    else:
        print("Numero non accettato (Minore di 0). Riprovare.")

fattoriale = 1

while int(num) > 1:
    fattoriale = fattoriale * num;
    num -= 1;
    
print(fattoriale);
