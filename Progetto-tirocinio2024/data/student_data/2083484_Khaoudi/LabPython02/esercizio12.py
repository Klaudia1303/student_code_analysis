#Scrivere un programma che:
#a. chiede all’utente di inserire in input nell’ordine un valore che rappresenta una temperatura ed un
#carattere tra ‘F’ e ‘C’, rappresentante la scala utilizzata per la temperatura (C= Celsius, F=
#Fahrenheit).
#b. Stampa a video lo stato dell’acqua alla temperatura indicata tra “solida”, “liquida” o “gassosa”.
#Nota: Si ricorda che l’acqua è solida quando la temperatura è minore o uguale a 0 ◦ C ed è gassosa se la
#temperatura è maggiore o uguale a 100 ◦ C.
#La formula per convertire la temperatura tra Celsius e Fahrenheit è: C = (F − 32)/1.8, dove C indica la
#temperatura in gradi Celsius e F indica la temperatura in gradi Fahrenheit.
car=input("Inserisci un carattere, C o F: ")
val=int(input("Inserisci un valore : "))
if(car == "C" and val >=100 or car=="F" and (val-32)/1.8>=100):
    print("Gassosa");
else:
    if(car==C and val <0 or car=="F" and (val-32)/1.8<0):
        print("Solida");
    else:
        print("Liquida");
