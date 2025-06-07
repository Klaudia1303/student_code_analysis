n1 = int(input("n1 (positivo): "))
while n1 <= 0:
    n1 = int(input("n1 (positivo): "))

n2 = int(input("n2 (positivo): "))
while n2 <= 0:
    n2 = int(input("n2 (positivo): "))

for i in range(n1, n2):
    if i % n1 == 0:
        print(i)
