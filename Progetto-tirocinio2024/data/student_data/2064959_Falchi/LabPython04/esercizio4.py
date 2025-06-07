n = None
Result = 0

while n != '0':
    n = input("Inserire valore: ")
    if ("+" in n or "-" in n) or n.isdecimal():
        if int(n) % 3 == 0:
            Result += int(n)
    else:
        print("ERRORE! Valore non valido.")
print("La somma dei numeri divisibili per 3 è:", Result)
