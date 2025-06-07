n = int(input("Inserire un numero intero strettamente maggiore di 2: "))
if n>2:
    i=2
    while i<=n:
        if i%2==0:
            print(i,"\n")
        i+=1
else:
    print("Input non valido!")