giorni = 0
distanza2 = 0

for giorni in range(1, 1001):
    distanza1 = 20*giorni
    distanza2 += giorni
    if distanza2 == distanza1:
        print(giorni)
        break
