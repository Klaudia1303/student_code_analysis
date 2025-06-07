n=str(input("Inserisci un numero: "))
counter=0
while not n=="*":
    n=int(input("Inserisci un numero: "))
    if n <0 :
        counter=counter+n
else:
    print("La somma è: ",counter)




