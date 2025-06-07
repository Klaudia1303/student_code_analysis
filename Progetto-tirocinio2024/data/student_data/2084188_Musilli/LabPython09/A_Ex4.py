def A_Ex4(filename,anno):
    fin=open(filename, encoding="UTF-8"); d={}
    riga1=fin.readline().strip().split(",");
    for c in riga1:
        if not(c.isalpha()):d[int(c)]=riga1.index(c)
    vmas=0; oggetto=""
    for elem in fin:
        elem=elem.strip().split(",");
        if int(elem[d[int(anno)]])>vmas:   vmas=int(elem[d[int(anno)]]); oggetto=elem[0]
        elif int(elem[d[int(anno)]])==vmas:  oggetto=max(oggetto, elem[0]);
    fin.close()
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
