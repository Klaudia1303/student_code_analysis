
velocitaPrimo = 20
velocitaSecondo = 1
distanza = 0
distanza2 = 0
for i in range(1,1000):
    distanza += velocitaPrimo
    distanza2 += velocitaSecondo
    if( distanza == distanza2):
        print('Il numero di giorni necessari per raggiungere il secondo sono :' + str(i))
        break
    velocitaSecondo += 1
