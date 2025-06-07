giorno=1
km1=20
km2=1
for n in range(2,1000):
    if km1 != km2:
        km1 += 20
        km2 += n
        giorno += 1
    else:
        break
print("Per raggiungerlo ci sono voluti ",giorno,"giorni per raggiungerlo")
