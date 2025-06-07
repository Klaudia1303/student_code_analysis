n=input("Inserisci un numero poitivo o negativo: ")
somma=0
while n!="0":
    if n[0]=="-":
        if int(n[1:])%3==0:
            somma=somma-int(n[1:])
    else:
        if int(n[0:])%3==0:
            somma=somma+int(n[0:])
    n=input("Inserisci un numero poitivo o negativo: ")
print(somma)
