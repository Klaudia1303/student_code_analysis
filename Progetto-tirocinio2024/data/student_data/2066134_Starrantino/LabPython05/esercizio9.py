n: int = int(input('> '))  # lato
print('*'*n)
for i in range(n-2):
    print('*' + ' ' * (n - 2) + '*')
print('*'*n)
