#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.7

s = input("Inserire una stringa: ");

test = False;


for i in range(0, len(s)):
    if s.count(s[i]) > 1:
        test = True;

print(test);