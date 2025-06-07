B=0
giorno=0
for giorno in range (1,10000):
    B=B+giorno
    A=20*giorno
    if B==A:
        print(giorno)
        break
