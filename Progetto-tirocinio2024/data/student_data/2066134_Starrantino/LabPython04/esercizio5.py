n: int = int(input('n >= 0: '))
out: int = 1

if n not in (0, 1):
    while n > 1:
        out *= n
        n -= 1

print(out)
