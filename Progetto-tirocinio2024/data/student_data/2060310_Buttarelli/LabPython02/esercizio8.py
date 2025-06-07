a = int(input("Inserisci il primo numero intero: "))
b = int(input("Inserisci il secondo numero intero: "))
c = int(input("Inserisci il terzo numero intero: "))
if a > 0 and b > 0 and c > 0 and a < b +c and b < a + c and c < a + b:
    if a == b and b == c:
        print("Triangolo equilatero.")
    else:
        if a == b and b != c or b == c and c != a or c == a and a != b:
            print("Triangolo isoscele.")
        else:
            print("Triangolo scaleno.")
else:
    print("Input non valido.")
