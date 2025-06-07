#Scrivere un programma che:
#a. chiede all’utente di inserire in input nell’ordine un valore che rappresenta una temperatura ed un
#carattere tra ‘F’ e ‘C’, rappresentante la scala utilizzata per la temperatura (C= Celsius, F=
#Fahrenheit).
#b. Stampa a video lo stato dell’acqua alla temperatura indicata tra “solida”, “liquida” o “gassosa”.
t = int(input("inserisci un valore di temperatura :"))
l = input("inserisci C per Celsius o F per Fahrenheit :")
if l=="C" :
    C= t
    F= 1.8*C+32
elif l=="F" :
    F= t
    C = (t-32)/1.8
else  :
    print("valore non valido")
if l=="C" or l=="F" :
    if C<=0 or F<=32 :
        print("solida")
    elif F>=212 or C>=100 :
        print ("gassosa")
    elif 32<F<212 or 0<C<100 :
        print("liquida")
    
        
