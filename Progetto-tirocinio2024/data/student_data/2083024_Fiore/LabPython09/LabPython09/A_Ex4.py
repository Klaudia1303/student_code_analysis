def A_Ex4(filename,anno):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f = open(filename,"r", encoding= "UTF-8")
    articolo = ""
    posizione = 0
    massimo = 0
    riga1 = f.readline().strip().split(",")
    for i in range(1,len(riga1)):
        if int(riga1[i]) == anno:
            posizione = i
    for riga in f:
        lista = riga.strip().split(",")
        if int(lista[posizione]) > massimo:
            massimo = int(lista[posizione])
            articolo = lista[0]
    return articolo
                    
     
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
