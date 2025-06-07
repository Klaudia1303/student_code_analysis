a=int(input("inserisci la lunghezza di un lato:"))
b=int(input("inserisci la lunghezza del secondo lato:"))
c=int(input("inserisci la unghezza del terzo lato:"))
if c>a+b or b>a+c or a>b+c:
    print("input non valido")
elif c<a+b or b<a+c or a<b+c:
    if c==b==a:
        print("triangolo equilatero")
    elif c!=a!=b:
        print("triangolo scaleno")
    elif c==a or c==b or b==a:
        print("triangolo isoscele")

