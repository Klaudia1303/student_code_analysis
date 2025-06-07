n = int(input('inserisci lato quadrato: '))
spazio = 0
for i in range(1, n + 1):
    if i == 1 or i == n:
        print('*' * n)
    else:
        print('*' + ' ' * (n - 2) + '*')
    
