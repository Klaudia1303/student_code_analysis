n = int(input("inserisci un lato: "))
for i in range(n):
    for j in range(n):
        if i==j or (i+j)==(n-1):
            print("*", end=" ")
        elif i==0 or j==0:
            print("*", end=" ")
        elif i==(n-1) or j==(n-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
