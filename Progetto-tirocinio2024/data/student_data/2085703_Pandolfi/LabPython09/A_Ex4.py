def A_Ex4(filename,anno):
    f = open(filename, "r")

    # cerco la posizione dell'anno che mi interessa
    riga = f.readline()
    indice = riga.strip().split(",")
    
    posizione = indice.index(str(anno))
    
    indice.clear()

    piuvenduto = ""
    quantita = 0

    while len(riga) > 0:
        riga = f.readline()
        lista = riga.strip().split(",")
        
        if lista[0] == "":
            break
        elif int(lista[posizione]) > quantita:
            quantita = int(lista[posizione])
            piuvenduto = lista[0]
        elif lista[posizione] == quantita:
            if lista[0] < piuvenduto:
                piuvenduto = lista[0]

    f.close()

    return piuvenduto

###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, ['Vendite1.csv',2012] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2012] , 'Maglione')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2013] , 'Zaino')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2011] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2010] , 'Cellulare')
    
    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
