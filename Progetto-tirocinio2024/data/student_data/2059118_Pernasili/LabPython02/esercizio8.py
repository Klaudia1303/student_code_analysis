a = int(input("Inserisci il primo lato: "))
b = int(input("Inserisci il secondo lato: "))
c = int(input("Inserisci un terzo lato: "))
if a < 0 or b < 0 or c < 0:
    print("input non valido")
if a> b+c or b> a+c or c > a+b:
        print("input non valido")
else:
    if a != b and b != c and a != c:
        print("E' un triangolo scaleno")
    if a == b and b!= c or a ==c and c!= b or c ==b and  b!= a:
        print("E' un triangolo isoscele")    
    if a == b and b == c:
        print("E' un triangolo equilatero")
        
