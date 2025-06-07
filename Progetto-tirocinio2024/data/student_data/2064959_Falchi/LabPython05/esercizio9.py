print("-- GENERATORE CONTORNI QUADRATI --\n")

l = input("Inserire valore lato: ")

if not l.isdecimal():
    print("ERRORE! Valore inserito non valido.")
    exit()
elif int(l) % 2 == 0 or int(l) < 3:
    print("ERRORE! Il lato deve avere un valore dispari e maggiore o uguale a 3.")
    exit()

print()

lato = int(l)

#Caratteri di disegno
drawingChar = '*'
spaceChar = " "

#Parametri di disegno (variano con il ciclo for)
draw = 1
spaces = (lato - 2)

#"Testina di stampa"
for i in range(1, lato + 1):
    if i == 1 or i == lato:
        print(drawingChar*lato)
    else:
        print(drawingChar*draw + spaceChar*spaces + drawingChar*draw)