vel_primo = int(input('Inserisci la velocità del primo viaggiatore: '))
vel_secondo = int(input('Inserisci la velocità del secondo viaggiatore: '))
primo = 0
secondo = 0
giorni = 0

for i in range(vel_secondo,1000,vel_secondo):
    primo += vel_primo
    secondo += i
    giorni += 1
    #print(primo,secondo,giorni)

    if primo <= secondo:
        break
    
print(giorni)
