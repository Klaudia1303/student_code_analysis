distanza1=20
distanza2=1
for giorno in range(2,1001):
    distanza2=distanza2+giorno
    distanza1=distanza1+20
    if distanza2>=distanza1:
        break
print(giorno)
