print("-- GENERATORE TRIANGOLI ISOSCELI --\n")

b = input("Inserire valore base: ")

if not b.isdecimal():
    print("ERRORE! Valore inserito non valido.")
    exit()
elif int(b) % 2 == 0 or int(b) < 3:
    print("ERRORE! La base deve avere un valore dispari e maggiore o uguale a 3.")
    exit()

print()

base = int(b)

#Caratteri di disegno
drawingChar = '*'
spaceChar = " "

#Parametri di disegno (variano con il ciclo for)
draw = 1
spaces = (base - 1)//2

#"Testina di stampa"
for i in range(1, base//2 + 2):
    print(spaceChar*spaces + drawingChar*draw)
    
    spaces -= 1
    draw += 2