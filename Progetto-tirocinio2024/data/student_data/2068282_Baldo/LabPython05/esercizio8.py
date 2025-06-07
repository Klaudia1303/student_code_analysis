n = int(input("inserisci la base del triangolo isoscele: "))
#dispari >= 3
m = n//2

for i in range(n+1):
    if i%2 != 0:
        k = " " * m + "*" * i
        m -= 1
        print(k)
