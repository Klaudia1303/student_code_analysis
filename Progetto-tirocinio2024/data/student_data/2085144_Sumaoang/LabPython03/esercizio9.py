n = int(input("Inserire un numero:"))

d = 2

isNumeroPrimo = True

while d<n:
    if n%d==0:
        isNumeroPrimo = False
    d = d+1

if isNumeroPrimo:
    print("numero primo")
else:
    print("numero non primo")

