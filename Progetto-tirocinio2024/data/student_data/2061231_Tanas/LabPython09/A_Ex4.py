def A_Ex4(filename,anno):
    f = open(filename,encoding='UTF-8')
    head = f.readline().strip().split(',')
    anno_ind = head.index(str(anno))

    max_prod, max_count = '', 0
    for l in f.readlines():
        data = l.strip().split(',')
        if int(data[anno_ind]) > max_count:
            max_prod = data[0]
            max_count = int(data[anno_ind])
        
        if int(data[anno_ind]) == max_count and data[0] < max_prod:
            max_prod = data[0]
    
    f.close()
    return max_prod
     
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
