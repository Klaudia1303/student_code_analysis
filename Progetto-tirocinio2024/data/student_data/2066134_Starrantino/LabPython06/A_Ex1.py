n1 = int(input('> '))
n2 = int(input('> '))
for d in range(n1, 0, -1):
    if n1 % d == 0 and n2 % d != 0:
        print(d)
