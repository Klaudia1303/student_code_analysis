def A_Ex4(filename,anno):
    fin=open(filename)
    m=0
    y=0
    L=[]
    prodotto='z'
    for riga in fin:
        riga=riga.strip().split(',')
        L.append(riga)
    for j in range(1,len(L[0])):
        if str(L[0][j])==str(anno):
            y=j
    for i in range(1,len(L)):
        if int(L[i][y])>=m and ord(str(L[i][0])[0])<ord(prodotto[0]):
            m=int(L[i][y])
            prodotto=L[i][0]
    fin.close()        
    return prodotto        
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
