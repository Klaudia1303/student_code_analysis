#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.9

numero=int(input("Inserire un numero: "));

if numero <=1 :
    print("Devi inserire un numero maggiore di 1")
else:
    div,count=2,0

while div <= numero/2 and count == 0:
    if numero%div == 0:
        count+=1;
        div+=1;
    if count==0:
        print("Numero primo!")
    else:
        print("Numero non primo!")