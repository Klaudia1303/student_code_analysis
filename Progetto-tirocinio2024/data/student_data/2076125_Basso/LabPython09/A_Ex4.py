def A_Ex4(filename,anno):
    f=open(filename)
    riga=f.readline()
    anni=riga.strip().split(',')
    print(anni)
    a=anni.index(str(anno))
    riga=f.readline()
    dati=riga.strip().split(',')
    m=0
    while len(riga)>0:
        if int(dati[a])>m:
            m=int(dati[a])
            oggetto=dati[0]
        elif int(dati[a])==m:
            if dati[0]>oggetto:
                m=int(dati[a])
                oggetto=dati[0]
        riga=f.readline()
        dati=riga.strip().split(',')
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
