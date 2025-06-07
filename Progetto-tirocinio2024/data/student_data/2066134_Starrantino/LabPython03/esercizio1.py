n = int(input('n > 2: '))
if n > 2:
    i: int = 2
    while i <= n:
        if i % 2 == 0:
            print(i)
        i += 1
