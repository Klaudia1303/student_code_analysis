a = int(input("inserisci il primo numero: "))
b = int(input("inserisci il secondo numero: "))
c = int(input("inserisci il terzo numero: "))
if a==b and a==c and b==c:
    print("triangolo equilatero")
elif a==b or a==c or b==c:
    print("triangolo isoscele")
else:
    print("triangolo scaleno")

