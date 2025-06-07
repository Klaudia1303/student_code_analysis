def A_Ex4(filename,anno):
    f = open(filename)
    anni = f.readline().strip().split(',')
    pos = anni.index(str(anno))
    s = f.readlines()
    massimo = 0
    maxven = 0
    for riga in s:
        l = riga.strip().split(',')
        if int(l[pos]) > int(massimo):
            massimo = l[pos]
            maxven = l[0]
        if int(l[pos]) == int(massimo):
            if l[0] > maxven:
                massimo = l[pos]
                maxven = l[0]
    f.close()
    return maxven
        
        
     
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
