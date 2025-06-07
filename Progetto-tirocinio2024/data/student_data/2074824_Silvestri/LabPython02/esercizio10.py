#10) Scrivere un programma che converte l’età del cane (input numero reale positivo) in età umana. Esempio:
#inserendo 10.0 il programma stamperà “53.0”.
#Nota: I primi due anni di vita di un cane equivalgono ciascuno a 10.5 anni di vita di un uomo, mentre per i
#successivi, ogni anno di vita di un cane equivale a 4 anni uomo. Gli anni non possono essere inferiori a 0.

var1=input('scopri quanti ammi umani ha il tuo cane!, inserisci gli anni del tuo cane: ')
var1=float(var1)

if var1>0 and var1<=2:
    print(var1*10.5)
elif var1>2:
    print(21+(var1-2)*4)
elif var1<=0:
    print('errore')
    
