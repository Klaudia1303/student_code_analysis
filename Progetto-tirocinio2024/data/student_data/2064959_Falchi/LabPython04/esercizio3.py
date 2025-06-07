n = None
Result = 0

while n != '*':
    n = input("Inserire un numero intero: ")

    if n == '*':
        break

    if ("+" in n or "-" in n) or n.isdecimal(): #Controllo validità valori.
        if int(n) < 0: #Il programma somma la variabile solo se il valore inserito è minore di 0.
            Result = Result + int(n)
    else:
        print("ERRORE! Carattere non valido.")


print("La somma dei numeri negativi è:", Result)
