n = " "
somma = 0
while n != "*":
        n = input("Inserire numeri interi (* per terminare):")
        if n != "*" and int(n) < 0:
            somma += int(n)
print(somma)
    

