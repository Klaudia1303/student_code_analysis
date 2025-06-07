n = int(input('Inserisci un intero: '))

print('*' * n)
for i in range(1, n - 1):
    s = '*' + ' ' * (n - 2) + '*'
    s = s[:i] + '*' + s[i + 1:]
    s = s[::-1][:i] + '*' + s[::-1][i + 1:]
    print(s)
print('*' * n)
