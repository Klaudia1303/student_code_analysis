n = int ( input("inserire un numero n: "))
m = int ( input("inserire un numero m: "))
somma = 0
if (n == 0 or m == 0):
    print ("il loro prodotto è 0")
if (m > 0):
    while m > 0:
        somma = somma + n
        m = m - 1
else:
    while m < 0:
        somma = somma + (-n)
        m = m + 1

print (somma)
