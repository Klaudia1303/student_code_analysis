velprimo=int(input('Velocità primo viaggiatore (chilomeri al giorno): '))
velsecondo=int(input('Velocità secondo viaggiatore (chilomeri al giorno): '))
kmprimo=0
kmsecondo=0
for i in range(1000):
    kmprimo=kmprimo+velprimo
    kmsecondo=kmsecondo+velsecondo
    velsecondo=velsecondo+1
    if kmsecondo>=kmprimo:
        break
print('Giorni necessari: ',i+1)

