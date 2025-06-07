def A_Ex4(filename,anno):
    f=open(filename)
    nomi=f.readline()
    nomilista=nomi.strip().split(',')
    
    
    maxp=0
    prodotto= ''
    colonaanno=nomilista.index(str(anno))

    for riga in f:
        riga=riga.strip().split(',')
        quantita=int(riga[colonaanno])
        if quantita>maxp:
            maxp=quantita
            oggetto=riga[0]

        elif quantita==maxp and riga[0]>=prodotto:
            prodotto=riga[0]


    return(oggetto)

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
