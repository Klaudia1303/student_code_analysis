def A_Ex4(filename,anno):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    oggetto = ''
    maxvenduti = 0
    f = open(filename, encoding="UTF-8")
    a = f.readline()
    i = a.strip().split(',').index(str(anno))
    for r in f:
        r = r.strip().split(',')
        if int(r[i])>maxvenduti or (int(r[i])==maxvenduti and r[0]>oggetto):
            oggetto = r[0]
            maxvenduti = int(r[i])
    f.close()

    return oggetto
 
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
