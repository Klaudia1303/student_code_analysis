n=int(input("Inserire un numero maggiore a 2: "))
while n<=2:
    n=int(input("Input errato. Inserire un numero maggiore a 2: "))
i=2
while i<=n:
    resto=i%2
    if resto==0:
        print(str(i)+"\n")
    i=i+1

