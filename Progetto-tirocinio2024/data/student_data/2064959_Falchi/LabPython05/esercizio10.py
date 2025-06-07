print("-- GENERATORE CONTORNI QUADRATI (CON DIAGONALI) --\n")

l = input("Inserire valore lato: ")

if not l.isdecimal():
    print("ERRORE! Valore inserito non valido.")
    exit()
elif int(l) < 2:
    print("ERRORE! Il lato deve avere un valore maggiore o uguale a 2.")
    exit()

print()

lato = int(l)

#Caratteri di disegno
drawingChar = "*" #'*'
spaceChar = " "

#Parametri di disegno (variano con il ciclo for)
draw = 1
spaces = (lato - 2)

#Cursore diagonale
pos = 2
ritorno = False

#"Testina di stampa"
lineDrawing = "" #Linea da stampare

for i in range(1, lato + 1):
    lineDrawing = "" #Azzeramento linea di stampa

    if i == 1 or i == lato:
        print(drawingChar*lato)
    else:
        for j in range(1, lato + 1):
            if j == 1 or j == lato:
                lineDrawing += drawingChar
            elif j == pos or j == lato + 1 - pos:
                lineDrawing += drawingChar
            else:
                lineDrawing += spaceChar
        
        pos += 1
        print(lineDrawing)