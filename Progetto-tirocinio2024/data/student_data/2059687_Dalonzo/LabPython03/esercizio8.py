

stringa = 'def'

while ( stringa[len(stringa) - 1::-1] != stringa):
    stringa = input('Inserire una stringa palindroma: ')

print('Stringa palindorma di lunghezza : ' + str(len(stringa)))