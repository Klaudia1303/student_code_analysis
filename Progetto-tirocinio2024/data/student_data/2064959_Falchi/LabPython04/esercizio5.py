n = input("Inserire valore: ")

Result = 1

if ("+" in n or "-" in n) or n.isdecimal(): #Controllo valori
    i = int(n)
    
    if i == 0:
        print(n + "! =", 1)
    elif i > 0:
        while i > 0:
            Result *= i
            i -= 1
        print(n + "! =", Result)
    else:
        print("(" + n + ")! = Indefinito")
else:
    print("ERRORE! Valore inserito non valido!")
