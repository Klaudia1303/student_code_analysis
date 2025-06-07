#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.7

s1 = input("Inserire la prima stringa: ");
s2 = input("Inserire la seconda stringa: ");
m = 0;
app = 0;
app2 = 0;
for i in range(len(s2)):
    for j in range(i+1,len(s2)):
        if s2[i:j] in s1 and len(s2[i:j]) >= m:
            m = len(s2[i:j]);
            papp2osi = i;
            app = j;
print(s2[app2:app]);