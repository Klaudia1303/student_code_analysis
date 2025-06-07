Valore = int(input("Inserire un numero intero divisibile per 5: "))

if Valore % 5 == 0:
    print(Valore // 5)

else:
    while Valore % 5 != 0:
        print(Valore, "non è divisibile per 5. Riprovare.")
        Valore = int(input("Inserire un numero intero divisibile per 5: "))

        if Valore % 5 == 0:
            print(Valore // 5)
