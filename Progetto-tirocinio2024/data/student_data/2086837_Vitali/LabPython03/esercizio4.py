x=int(input("Inserisci intero x: "))
y=int(input("Inserisci intero y: "))
while x<0 or x>10:
    print("Valore della x non valido")
    x=int(input("Inserisci intero x: "))
while y<0 or y>10:
    print("Valore della y non valido")
    y=int(input("Inserisci intero y: "))
i=0
while i<=10:
    if i!=x and i!=y:
        print("\n",i)
    i +=1
    
