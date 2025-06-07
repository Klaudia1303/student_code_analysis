n1 = int(input('inserisci un intero: '))
n2 = int(input('inserisci un secondo intero: '))
i = 0
for i in range(1, n2):
    if i % n1 == 0:
        print(i)
