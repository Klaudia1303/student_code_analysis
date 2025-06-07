s = input("Inserisci un intero (* per terminare): ")
counter = 0
while s != "*":
    num = int(s)
    if num >= 0:
        counter += 1
    s = input("Inserisci un intero (* per terminare): ")
print(counter)
