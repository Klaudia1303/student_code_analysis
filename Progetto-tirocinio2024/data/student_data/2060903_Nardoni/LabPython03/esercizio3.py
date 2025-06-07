controllo=False
while not controllo:
    n=int(input("Inserisci un numero intero (termina inserendo un numero divisibile per 5)"))
    if n%5==0:
        print(n/5)
        controllo=True
