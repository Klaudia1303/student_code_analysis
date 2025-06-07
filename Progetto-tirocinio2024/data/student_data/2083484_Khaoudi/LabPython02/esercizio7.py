#Scrivere un programma che legge in input 3 numeri interi, n1, n2, n3, e li stampa in ordine decrescente. Ad
#esempio, se n1=9, n2=14, n3=10, il programma deve stampare prima 14, poi 10 e successivamente 9, ossia
#“14
#10
#9”.
n1=int(input("Inserisci un numero: "));
n2=int(input("Inserisci un numero: "));
n3=int(input("Inserisci un numero: "));
if(n1>n2):
    if(n2>n3):
        print(n1,n2,n3);
    else:
        print(n1,n3,n2);
else:
    if(n2>n3):
        if(n3>n1):
            print(n2,n3,n1);
        else:
            print(n2,n1,n3);
    else:
        print(n3,n2,n1);
        

