n = int(input("Inserisci un numero intero (inserire un multiplo di 5 per terminare): "))
while n % 5 != 0:
    n = int(input("Inserisci un numero intero (inserire un multiplo di 5 per terminare): "))
div = n // 5
print("Risultato della divisione tra", n," e 5:", div)
    
