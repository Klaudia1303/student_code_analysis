n = int(input("inserisci un numero dispari maggiore di 1: "))
for i in range(1, (n + 1), 2):
    a = ((n - i) // 2)*' '
    print(a + i*'*')
