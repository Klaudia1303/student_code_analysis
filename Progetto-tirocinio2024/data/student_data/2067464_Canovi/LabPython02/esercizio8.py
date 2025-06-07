a = input("inserisci un valore intero: ")
a = int(a)
b = input("inserisci un valore intero: ")
b = int(b)
c = input("inserisci un valore intero: ")
c = int(c)

if a > 0 and b > 0 and c > 0:
    if a < (b + c) and b < (a + c) and c < (a + b):
        if a != b != c:
            print("scaleno")
        elif a == b != c:
            print("isoscele")
        elif a == b == c:
            print("equilatero")
    else:   print("input non valido")

else:   print("input non valido")
