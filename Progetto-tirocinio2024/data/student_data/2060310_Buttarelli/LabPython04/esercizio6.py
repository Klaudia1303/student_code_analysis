n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))
i = 0
m = 0
while i != abs(n2):
    if n1 >= 0:
        m += n1
    else:
        if n1 < 0:
            m += abs(n1)
    i += 1
if n1 < 0 or n2 < 0:
    print(n1, " * ", n2, " = ", (-m))
else:
    print(n1, " * ", n2, " = ", m)
