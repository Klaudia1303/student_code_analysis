n = int( input("inserire un numero intero n: "))
i = 1
i = int(i)
somma = 0
while i <= n:
    if (n%i == 0):
        somma = somma +1
    i = i + 1
if (somma == 2 or somma == 1):
    print("numero primo")
else:
    print ("numero non primo")
