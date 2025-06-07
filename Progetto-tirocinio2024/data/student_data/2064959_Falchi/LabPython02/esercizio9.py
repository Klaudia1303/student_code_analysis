m = int(input("Inserire primo valore: "))
y = int(input("Inserire secondo valore: "))

if 1 <= m <=12:
    if m < 12:
        m = m + 1
        print(m, "/", y)
    elif m == 12:
        m = 1
        y = y + 1
        print(m, "/", y)
else:
    print("input non valido")
