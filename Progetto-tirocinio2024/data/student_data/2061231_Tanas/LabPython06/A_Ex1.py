n1 = 0
while n1 <= 0:
    n1 = int(input("inserisci n1: "))

n2 = 0
while n2 <= 0:
    n2 = int(input("inserisci n2: "))

for i in range(n1, 1, -1):
    if n1 % i == 0 and n2 % i != 0:
        print(i)
