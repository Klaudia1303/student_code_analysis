n=int(input("inserire un numero maggiore di 0: "))
numero=0
if n>0:
    while numero<=n:
        numero=numero+1
        if n%numero==0:
            print(numero)
else:
    print("errore")
