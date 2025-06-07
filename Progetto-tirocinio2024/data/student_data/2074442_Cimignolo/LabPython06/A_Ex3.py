for i in range(1, 9):
    for j in range(1, 9):
        prodotto = i * j
        risultato = ''
        while True:
            if (prodotto == 0):
                break
            risultato += str(prodotto % 8)
            prodotto //= 8

        newI = str(i)
        newJ = str(j)
        if (i < 8):
            newI = '0' + str(i)
        else:
            newI = '10'
        if (j < 8):
            newJ = '0' + str(j)
        else:
            newJ = '10'

        if (int(risultato[::-1]) < 8):
            risultato += '0'
        
        print(risultato[::-1], end='   ')
    
    print('\n\n')
