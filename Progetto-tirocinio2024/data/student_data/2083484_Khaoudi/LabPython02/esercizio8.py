#Scrivere un programma che prende in ingresso 3 interi a, b, c, e determina se essi possano rappresentare le
#lunghezze dei lati di un triangolo (cioè se siano tutti positivi, e se ciascuno sia minore della somma degli altri
#due); in caso affermativo stampare il tipo del triangolo tra “scaleno”, “isoscele”, “equilatero”, in caso
#negativo “input non valido”.
a = int(input("Lato: "));
b = int(input("Lato: "));
c = int(input("Lato: "));

if(a>0 and b>0 and c>0):
    if(a+b<c or a+c<b or b+c<a):
        print("Input non valido");
    else:
        if(a==b and b==c):
            print("Equilatero");
        else:
            if(a==b or b==a or c==a):
                print("Isoscele");
            else:
                print("Scaleno");
else:
    print("Input non valido");


