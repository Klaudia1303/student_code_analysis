#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.8

s1=input("Inserire prima stringa: ");
s2=input("Inserire la seconda stringa: ");

n=int(input("Inserire un numero: "));

s=''
for i in range(len(s1)):
    f=s2.find(s1[i]);
    if f==-1:
        continue;
    

    if f-i<=n and i-f<=n:
        s=str(s)+str(s1[i]);

print(s);