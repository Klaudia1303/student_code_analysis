n1 = int(input('n1: '))
n2 = int(input('n2: '))
n3 = int(input('n3: '))
a = max(n1, n2, n3)
b = min(n1, n2, n3)
c = n1+n2+n3-a-b
print('', a, '\n', c, '\n', b)
