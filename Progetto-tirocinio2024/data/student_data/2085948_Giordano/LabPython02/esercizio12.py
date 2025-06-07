from tkinter import Variable


x=int(input("Inserisci il valore della temperatura: "))
y=input("Scegli l'unità di misura tra C ed F: ")
if y=="F":
    x=(x-32)%1.8
    if x>=100:
        print("Gassosa")
    if x<=0:
        print("Solida")
    else:
        print("Liquida")
