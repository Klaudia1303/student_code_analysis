n=int(input("Inserire un numero maggiore di 2:  "))
if n<=2:
    print("Errore")
else:
    i=2
    while n>i:
        if i%2==0:
            print(i)
        i=i+1

