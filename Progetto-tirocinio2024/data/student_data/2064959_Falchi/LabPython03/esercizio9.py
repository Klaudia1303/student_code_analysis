Primo = False

n = int(input("Inserire un numero n: "))
i = 2

count = 0

while i < n:
    if n % i != 0:
        count = count + 1
    i = i + 1

if count + 2 == n:
    Primo = True

if Primo:
    print("numero primo")
else:
    print("numero non primo")
