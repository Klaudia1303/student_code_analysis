print("Il primo viaggiatore viaggia alla velocità di 20 km al giorno")
print("Il secondo viaggiatore viagga alla velocità di 1 km il primo, 2 il secondo e così via")
giorni=0
n2=0
for i in range(1,1000):
    n1 = 20*i
    n2 = n2 + i
    giorni = i
    if n1 == n2:
        break
print("Il giorno in cui il secondo viaggiatore incontrerà il primo è "+str(giorni))
