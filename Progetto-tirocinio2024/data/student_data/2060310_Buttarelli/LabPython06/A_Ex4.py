v1 = 0
v2 = 0
giorni = 0
for i in range(1, 1000):
    v1 += 20
    v2 += i
    if v1 == v2:
        giorni = i
        break
print("Il secondo viaggiatore ha raggiunto il primo! Giorni passati:", giorni)
