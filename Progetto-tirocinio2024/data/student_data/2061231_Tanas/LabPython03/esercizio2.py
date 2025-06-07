n = 0
while not n > 0:
    n = int(input("numero: "))

div = 1
while div <= n:
    if n % div == 0:
        print(div)
    div += 1
