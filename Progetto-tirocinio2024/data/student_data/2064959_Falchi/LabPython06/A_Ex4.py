v1 = 20
v2 = 1

d1 = 20
d2 = 1

giorni = 1

superato = False

for i in range(1000):
    #print(d1)
    #print(d2)
    if  d1 >= d2 and superato:
        print("Arrivato!")
        break
    d1 += v1
    v2 += 1
    d2 += v2

    if d2 >= d1:
        superato = True

    giorni += 1

print(giorni)
