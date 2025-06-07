n1 = int(input("Numero intero: "))
n2 = int(input("Numero intero: "))

for i in range(n1,1,-1):
    if n1%i == 0 and n2&i != 0:
        print(i)
