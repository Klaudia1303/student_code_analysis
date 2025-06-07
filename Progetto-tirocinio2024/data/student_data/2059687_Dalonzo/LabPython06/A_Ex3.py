
prodotto = 0
resto = 100
final = ''
for i in range(1,9):
    for c in range(1,9):
        prodotto = i * c
        if(prodotto > 7):
            quoziente = prodotto
            while(resto > 0):
                #print('Il resto è :' + str(resto) + ' e il quoziente :' + str(quoziente))
                if(prodotto % 8 == 0):
                    final += str(0) + str(quoziente // 8)
                    break
                resto = quoziente % 8
                quoziente -= resto
                if(resto == 0):
                    final += str(quoziente // 8)
                else:
                    final += str(resto)
            print(final[len(final)::-1],end=' ')
            final = ''
            resto = 100
        else:
            final = '0' + str(prodotto)
            print(final,end=' ')
            final = ''
            

    print('\n')
