userinput = input("Inserisci un numero intero: ")
i = 0

while userinput != "*":
    n = int(userinput)
    if n < 0:
        i += n
    userinput = input("Inserisci un numero intero: ")

print(i)
