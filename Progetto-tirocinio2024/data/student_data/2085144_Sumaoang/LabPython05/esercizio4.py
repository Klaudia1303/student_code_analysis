n1 = int(input("Inserire un numero intero positivo:"))
n2 = int(input("Inserire un numero intero positivo:"))
i = True
m = 1
x = 1
while i == True :
        m = n1 * x
        if m > n2:
                i = False
                break
        print(m)
        x += 1
