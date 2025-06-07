#Scrivere un programma che prenda in ingresso un intero (a) e una stringa (s) e stampa la stringa solo se a è
#dispari
a = int(input("inserisci un numero :") )
s = str(input("inserisci una parola :") )
if a%2==1 :
    print(s)
else : print ("riprova")
