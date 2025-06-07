n = int(input("Inserire un numero intero maggiore o uguale a 3:"))
s = " "

print("*" * n)

for x in range(n-2):
    print( "*" + s * (n-2) + "*" )

print("*" * n)


