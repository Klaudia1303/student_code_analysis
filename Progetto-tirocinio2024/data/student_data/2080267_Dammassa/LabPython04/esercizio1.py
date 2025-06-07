s = 0
finito = False
a = "a"
c = "c"
while not finito:
    n = input("inserisci una stringa: ")
    s += 1
    if a and c in n:
        finito = True
        print(s)
