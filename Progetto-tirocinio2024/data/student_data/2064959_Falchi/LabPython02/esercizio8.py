a = int(input("Inserire valore 'a': "))
b = int(input("Inserire valore 'b': "))
c = int(input("Inserire valore 'c': "))

if (a > 0 and b > 0 and c > 0) and (a < b + c and b < a + c and c < a + b):
    if ((a != b and b != c) and b != a and a != c and c != a and a != b):
        print("Il triangolo è scaleno.")
    elif ((a == b and a != c) or (a == c and a != b) or (c == b and c != a)):
        print("Il triangolo è isoscele.")
    elif a == b and b == c:
        print("Il triangolo è equilatero.")
else:
    print("input non valido")
