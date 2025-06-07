#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.10

dim = input("Inserire lato del quadrato: ");

for i in range(int(dim)):
    for j in range(int(dim)):
        if i == 0 or i == int(dim)-1 or j == 0 or j == int(dim)-1 or j == i or j == int(dim)-1-i:
            print("*",end="");
        else:
            print(" ",end="");
    print("");