n = str(input("Inserisci un numero intero (* per terminare): "))
positivi = 1
while n != "*":
    n = str(input("Inserisci un numero intero (* per terminare): "))
    if n!= "*":
        n = int(n)
        if n > 0:
            positivi += 1
    n = str(n)
print("Numeri positivi inseriti:", positivi)
