n = int(input("Numero: "))
if n <= 1:
    print("Input non valido")
else:
    i = 2
    while i <= n:
        j = 2
        primo = True
        while j < i and primo:
            if i % j == 0:
                primo = False
            j += 1
        if primo:
            print(i)
        i += 1
