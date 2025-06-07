#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.5

test = True;

while test:
    s = input("Inserire una stringa: ");
    n = input("Inserire un numero: ");

    if len(s) < 2:
        print("La stringa deve essere composta da almeno due caratteri. Riprovare.");
    else:
        test = False;

for i in range(0, len(s)-int(n)):
    carattere = s[i];
    if carattere == s[i+int(n)]:
        print("True");
    else:
        print("False");
    i += int(n);
