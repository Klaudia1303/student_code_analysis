


stringa = '  '
caratt = input('Inserire un carattere:')


while(stringa.count(caratt) <= 2):
    stringa = input('Inserire una stringa : ')
    print('Numero di occorrenze del carattere ' + caratt + ' in :' + stringa + ' : ' + str(stringa.count(caratt)))
    