stringa = input('inserisci stringa: ')
contatore=0
ripetizioni=0
maggiore=0
mezzo=0

while contatore<len(stringa):
    carattere=stringa[contatore]
    ripetizioni=stringa.count(carattere)
    if ripetizioni>=mezzo:
        mezzo=ripetizioni
        maggiore=carattere
    contatore+=1

print(maggiore)
