print("ESERCIZIO 8: inserimento dei 3 lati di un triangolo \
(devono essere interi, >0 e ogni lato deve essere inferiore alla somma \
degli altri due) e dire se Equilatero, Scaleno o Isocele\n")
a=int(input("Inserire il primo lato di un triangolo: \t"))
b=int(input("Inserire il secondo lato di un triangolo: \t"))
c=int(input("Inserire il terzo lato di un triangolo: \t"))
if a>0 and b>0 and c>0:
    if a<=b+c and b<=a+c and c<=a+b:
        if a==b and a==c and b==c:
            print("Il triangolo è equilatero")
        elif a==b or a==c or b==c:
            print("Il triangolo è isocele")
        else:
            print("Il triangolo è scaleno")
    else:
        print("Dati inseriti non validi,\
i singoli lati non sono inferiori alla somma degli alri due. \n\
Quindi non si ha un triangolo\n")
else:
    print("Dati inseriti non validi, i lati sono negativi\n")
