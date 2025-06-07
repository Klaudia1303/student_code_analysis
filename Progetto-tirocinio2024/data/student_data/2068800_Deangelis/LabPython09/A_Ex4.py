def A_Ex4(filename,anno):
    f=open(filename, 'r')
    max=0
    for elem in f:
        elem=elem.strip().split(',')
        if elem[0]=='Anno':
            pos=elem.index(str(anno))
        if elem[0]!='Anno':
            if int(elem[pos])>int(max):
                max=elem[pos]
                oggetto=elem[0]
            if (elem[pos])==int(max) and len(oggetto)<len(elem[0]):
                max=int(elem[pos])
                oggetto=elem[0]   
    return(oggetto)

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
