i = 0
finito = False
while not finito:
    n = input("Inserisci un numero intero(* per terminare): ")
    if n == "*":
        finito = True
        print(i)
    if n != "*" and int(n) > 0:
        i += 1
