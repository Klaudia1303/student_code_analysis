a = input("a: ")
a = int(a)
b = input("b: ")
b = int(b)
c = input("c: ")
c = int(c)
if a<(b+c) and b<(a+c) and c<(a+b) and a != b != c :
    print("'a', 'b', e 'c' sono possibili lati di un triangolo scaleno")
elif a<(b+c) and b<(a+c) and c<(a+b) and (a==b != c or a==c != b or b==c != a) :
    print("'a', 'b', e 'c' sono possibili lati di un triangolo isoscele")
elif a<(b+c) and b<(a+c) and c<(a+b) and a == b == c :
    print("'a', 'b', e 'c' sono possibili lati di un triangolo equilatero")
else :
    print("input non valido")
