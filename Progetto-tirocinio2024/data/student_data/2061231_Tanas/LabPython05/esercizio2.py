s = input("stringa: ")
n = int(input("intero positivo: "))

while n <= 0:
    n = int(input("intero positivo: "))

for c in s:
    print(c*n,end='')

