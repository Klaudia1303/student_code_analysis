#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.6

from tkinter import N


ncaratteri = 1

while ncaratteri < 1:
    print("Inserisci una stringa da almeno un carattere: ",end="");
    stringa = input();
    ncaratteri = len(stringa);
    if ncaratteri < 1:
        print("La stringa deve essere più lunga. Riprovare");

test = True;

while test == True:
    for n in range(ncaratteri):
        codice = stringa.encode('utf-8');
        if int(codice) > 100:
            test = False;
            print("trovato carattere con codice Unicode maggiore di 100. Il codice tro")
    n = int(n) + 1;
print("Stringa consumata e carattere non trovato.");