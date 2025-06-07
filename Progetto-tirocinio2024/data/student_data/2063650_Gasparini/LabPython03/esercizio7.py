c = input("Carattere: ")
finito = False
while not finito:
    s = input("Stringa: ")
    occorrenze = s.count(c)
    if occorrenze > 2:
        finito = True
        print(occorrenze)
