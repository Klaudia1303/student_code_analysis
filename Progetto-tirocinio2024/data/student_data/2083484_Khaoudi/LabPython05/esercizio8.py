n=int(input("Inserisci un numero dispari uguale o superiore a 3 : "))

i=1
while i<=n:
    spaces=int((n-i)/2)
    string=" "*spaces+"*"*i+" "*spaces
    i+=2
    print(string)
