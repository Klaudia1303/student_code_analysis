cane = float(input('inserire età cane: '))
if cane>=0:
    if cane<=2:
        print(cane*10.5)
    elif cane>2:
        print(10.5*2+(cane-2)*4)
else:
    print('errore: età del cane inferiore a 0')
