numero= int(input("inserisci un numero : "))
if numero>0:
    preced1=1
    preced2=1
    i=2
    while i<=numero:
        if numero==0 or numero==1: 
            print(1)
        else:
            somma=preced1+preced2
            print(somma)
            preced1=preced2
            preced2=somma
        i=i+1
else:
    print("hai inserito un numero negativo")
