n=int(input("Inserire un numero maggiore a 0: "))
while n<=0:
    n=int(input("Input errato. Inserire un numero maggiore a 0: "))
i=1
while i<=n:
    resto=n%i
    if resto==0:
        print(str(i))
    i=i+1
