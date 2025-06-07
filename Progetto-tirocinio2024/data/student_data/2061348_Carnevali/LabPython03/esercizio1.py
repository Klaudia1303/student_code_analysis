n=int(input("inserire un intero maggiore di 2: "))
numero=int(2)
if n>2:
    while numero<=n:
        print(numero)
        numero=numero+2
else:
    print("errore")
