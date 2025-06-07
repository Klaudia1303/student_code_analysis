#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.6

s = input("Inserire una stringa: ");
max = 0;

for i in range(len(s)):
    distanza = s.rfind(s[i])-i;
    #print(s[i], int(distanza));
    if distanza > max:
        max = distanza;
print(max);