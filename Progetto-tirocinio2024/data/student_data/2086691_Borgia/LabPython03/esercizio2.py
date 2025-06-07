numero=int(input("Inserire un numero intero maggiore di 0: "))
i=1
while i<=numero:
    if numero%i==0:
        print(i)
    i+=1
