#Scrivere un programma che converte l’età del cane (input numero reale positivo) in età umana. Esempio:
#inserendo 10.0 il programma stamperà “53.0”.
#Nota: I primi due anni di vita di un cane equivalgono ciascuno a 10.5 anni di vita di un uomo, mentre per i
#successivi, ogni anno di vita di un cane equivale a 4 anni uomo. Gli anni non possono essere inferiori a 0.
eta=float(input("Inserisci l'età: "))
if(eta==0):
    print("Input non valido")
else:
    if(eta<=2):
        print(eta*10.5)
    else:
        print(21+(eta-2)*4)
