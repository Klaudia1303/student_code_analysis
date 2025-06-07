n1 = int(input('inserisci numero:'))
n2 = int(input('inserisci numero:'))




for i in range(8):
    for l in range(8):
        print(i, "*", l ," = ",oct(i*l)[2:])
