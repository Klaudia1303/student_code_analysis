#Scrivere un programma che converte l’età del cane (input numero reale positivo) in età umana. Esempio:
#inserendo 10.0 il programma stamperà “53.0”.
#Nota: I primi due anni di vita di un cane equivalgono ciascuno a 10.5 anni di vita di un uomo, mentre per i
#successivi, ogni anno di vita di un cane equivale a 4 anni uomo. Gli anni non possono essere inferiori a 0.

cane= int(input('età del cane: '))

if cane<=2:
    print(cane*10.5)
elif (cane>2):
    print(21+(cane-2)*4)
