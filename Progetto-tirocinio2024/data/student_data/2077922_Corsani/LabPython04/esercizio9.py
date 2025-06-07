#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.9

test = True
while test:
    num = int(input('Inserire un numero: '))
    if int(num) >= 0:
        test = False;
    else:
        print("Numero non accettato (Minore di 0). Riprovare.");
countprec = 0;
count = 0;
for i in range(0, num):
    if int(i) < 1:
        a = b = 1;
        print(count);
    else:
        a = b;
    b = count;
    count = a + b;
    print(count);
    i += i;