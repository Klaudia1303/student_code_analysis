n1 = int(input('inserisci intero positivo: '))
n2 = int(input('inserisci intero positivo: '))
divisore_n1 = 0

for i in range(n1, 0, -1):
    if n1%i == 0 and n2%i != 0:
        divisore_n1 = i
        print(divisore_n1)
