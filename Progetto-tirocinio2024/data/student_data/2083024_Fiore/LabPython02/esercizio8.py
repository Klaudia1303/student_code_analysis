print("inserisci le misure di 3 lati per fomrare un triangolo")
a = float(input("inserisci primo lato: "))
b = float(input("inserisci secondo lato: "))
c = float(input("inserisci terzo lato: "))

if (a and b and c) > 0:
    if a < (b+c) and b < (a+c) and c < (a+b):
        if a != b and a != c and c != b:
            print("Il triagolo è scaleno")
        elif a == b and a != c:
            print("il triangolo è isoscele")
        elif a == c and a != b:
            print("il triangolo è isoscele")
        elif b == c and b != a:
            print("il triangolo è isoscele")

        elif a == b and b == c and c == a:
            print("il triangolo è equilatero")


