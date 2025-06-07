n = int(input("Inserire un numero intero (>0): "))
n1 = n2 = 1
i = 2
if n == 1:
    print(n1)
elif n > 1:
    print(n1,n2, sep="\n")
while i < n:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3)
    i += 1
