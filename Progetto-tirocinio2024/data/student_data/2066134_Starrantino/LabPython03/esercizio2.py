i: int = 1
n = int(input('n > 0: '))
while i <= n:
    if n % i == 0:
        print(i)
    i += 1