def A_Ex4(filename,anno):
    ris = []
    f = open (filename, "r", encoding = "UTF-8")
    verifica = f.readline()
    verifica = verifica.strip().split(",")
    anno = str(anno)
    index = (verifica.index(anno))
    
    for riga in f:
        riga = riga.strip().split(",")
        ris.append(riga)
    
    massimo = 0
    oggetto = 0
    for j in range (0, len(ris)):
        if int(ris[j][index]) > massimo:
            massimo = int(ris[j][index])
            oggetto = ris[j][0]
        elif int(ris[j][index]) == massimo and ris [j][0] > oggetto:
            oggetto = ris[j][0]
    f.close()
    return oggetto
        
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
     
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
