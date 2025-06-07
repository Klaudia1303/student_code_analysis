n, n2 = int(input('n: ')), int(input('n2: '))
out: int = sum([abs(n) for _ in range(abs(n2))])
out = -out if [n < 0, n2 < 0].count(True) == 1 else out
print(out)