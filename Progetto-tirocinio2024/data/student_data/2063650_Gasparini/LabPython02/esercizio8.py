a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if min(a, b, c) <= 0 or a + b < c or a + c < b or b + c < a:
    print("input non valido")
elif a == b or b == c or a == c:
    if a == b and a == c:
        print("equilatero")
    else:
        print("isoscele")
else:
    print("scaleno")
        
