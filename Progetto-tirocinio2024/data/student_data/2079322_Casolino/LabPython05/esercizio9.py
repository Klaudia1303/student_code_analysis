#Scrivere un programma che chiede in input all’utente la dimensione
#del lato di un quadrato (assumete che sia un intero dispari maggiore o uguale
#a 3) e ne disegna sullo schermo il contorno, usando il carattere ‘*’.
#Ad esempio, inserendo l’intero “5” per il lato del quadrato,
#il programma produce a schermo il seguente disegno
#*****
#*   *
#*   *
#*   *
#*****
#ottenuto stampando cinque ‘*’, a capo un ‘*’ tre spazi e un ‘*’,
#a capo un ‘*’ tre spazi e un ‘*’, a capo un ‘*’ tre spazi e un ‘*’,
#a capo cinque ‘*’.

l = int(input("Inserire il lato del quadrato bucato: "))
if l%2!=0 and l>=3:
    for i in range(l):
        print('*', end='')
    print()
    for k in range(l-2):
        print('*', end='')
        for i in range(l-2):
            print(' ', end='')
        print('*')
    for i in range(l):
        print('*', end='')
    print()
else:
    print("Il lato non è un intero dispari maggiore od uguale a 3")
