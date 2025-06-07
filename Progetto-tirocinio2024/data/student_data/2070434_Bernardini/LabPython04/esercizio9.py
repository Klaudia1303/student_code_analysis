n = int(input("Inserire un numero intero (>0): "))
a = b = 1
i = 2
if n == 1:
    print(n1)
elif n > 1:
    print(a,b, sep="\n")
while i < n:
    c = a + b
    a = b
    b = c
    print(c)
    i += 1
