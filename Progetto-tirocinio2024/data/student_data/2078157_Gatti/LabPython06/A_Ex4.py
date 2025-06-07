g1 = 0
g2 = 0
for i in range(1, 1001):
    g1 = g1 + 20
    g2 = g2 + i
    if g2 >= g1:
        print('numero di giorni =' , i)
        break
    
    
