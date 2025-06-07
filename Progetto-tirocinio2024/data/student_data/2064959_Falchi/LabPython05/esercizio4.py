n1 = int(input("Inserire il primo numero intero: "))
n2 = int(input("Inserire il secondo numero intero: "))

for i in range(1, n2):
    if i*n1 < n2:
        print(i*n1)