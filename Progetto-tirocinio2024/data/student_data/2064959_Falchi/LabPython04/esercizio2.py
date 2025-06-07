n = None
n_count = 0

while n != '*':
    n = input("Inserire un numero intero: ")

    if n == '*':
        break
        
    if ("+" in n or "-" in n) or n.isdecimal(): #Controllo valori.
        if int(n) > 0: #Il programma incrementa la variabile solo se il valore inserito è maggiore di 0.
            n_count += 1
    else:
        print("ERRORE! Carattere non valido.")

    
print("Sono stati inseriti", n_count, "numeri positivi.")
