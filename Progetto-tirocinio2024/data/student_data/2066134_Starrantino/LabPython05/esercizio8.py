n: int = int(input('> '))  # base
for ast in range(1, n+1, 2):
    print(' ' * ((n - ast) // 2) + '*' * ast)
