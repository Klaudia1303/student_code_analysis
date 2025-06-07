#Scrivere un programma che chiede in input all’utente la dimensione
#del lato di un quadrato (un intero maggiore o uguale a 2)
#e ne disegna sullo schermo il contorno e le due diagonali,
#usando il carattere ‘*’. Ad esempio, inserendo l’intero “5”
#per il lato del quadrato, il programma produce a schermo il seguente disegno
#*****
#** **
#* * *
#** **
#*****
#ottenuto stampando:
#cinque ‘*’, a capo
#due ‘*’, uno spazio, due ‘*’, a capo
#un ‘*’, uno spazio, un ‘*’, uno spazio, un ‘*’, a capo due ‘*’,
#uno spazio, due ‘*’, a capo
#cinque ‘*’

l=int(input("Inserire la misura del lato del quadrato:"))
if l>=2:
    for i in range(l):
        for j in range(l):
            if i==0 or i==l-1:
                print('*', end='')
            elif j==0 or j==l-1:
                print('*', end='')
            elif j==i or j==l-1-i:
                print('*', end='')
            else:
                print(' ', end='')
        print()
