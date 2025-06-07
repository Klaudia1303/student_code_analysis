n = int(input('inserisci la lunghezza della base di un triangolo isoscele (dispari e maggiore di 3): '))
spaziopiù = 0
for i in range(1, n + 1, 2):
    spazio = ' ' * ((n - 1) // 2 - spaziopiù)
    spaziopiù += 1
    print(spazio, '*' * i, spazio)
    


