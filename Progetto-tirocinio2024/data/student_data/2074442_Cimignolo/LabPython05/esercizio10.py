lato=int(input('inserisci la dimensione del lato: '))

print('*'*lato)
for i in range(1,lato-1):
    d= '*' + ' ' * (lato - 2) + '*'
    d=d[:i] + '*' + d[i + 1:]
    d=d[:lato - 1 - i] + '*' + d[lato - i:]
    print(d)

print('*'*lato)
