
countMax = 0
stringa = input('Inserire una stringa alfanumerica : ')
count = 1
caratt = stringa[0]

for i in range(0,len(stringa)):
    for c in range(i,len(stringa) - 1):

        carattTemp = stringa[i]
        stringaTemp = stringa[c + 1::]
        if(stringaTemp.find(carattTemp) == 0):
            print('Trovo in posizione :' + str(c) + ' , carattere :' + carattTemp)
            count += 1
            if(count >= countMax):
                caratt = carattTemp
                countMax = count
            continue
        else:
            count = 1
            break


print('Il carattere con piu occorrenze consecutive (' + str(countMax) + ') è :' + str(caratt))
