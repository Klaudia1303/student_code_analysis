

oldStringa = ' '
trovato = False
while(trovato == False):
    stringa = input('Inserire una stringa')
    if(stringa[0] == oldStringa[len(oldStringa) - 1]):
        print('penultima stringa :' + oldStringa + ', ultima stringa :' + stringa)
        trovato = True
    oldStringa = stringa
