n=int(input('inserire un numero disparo positivo: '))
for c in range(n):   
        print("*", end="")
print()
for r in range(n-2):   
    print("*", end="")
    for c in range(n-2):
        print(" ", end="")
    print("*")
for c in range(n):  
    print("*", end="")
print()
