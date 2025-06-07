l = int(input("Lato: "))

for y in range(l):
    for x in range(l):
        if x == 0 or y == 0 or x == l - 1 or y == l - 1 or x == y or x == l - 1 - y:
            print("*", end="")
        else:
            print(" ", end="")
    print()
