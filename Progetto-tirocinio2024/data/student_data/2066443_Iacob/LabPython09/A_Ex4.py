def A_Ex4(filename,anno):
    o = open(filename, 'r', encoding='UTF-8')
    l = []
    for line in o:
        line = line.strip().split(',')
        l.append(line)
    
    y = l[0]
    obj = l[1:]
    
    pos = 0
    for a in range(len(y)):
        if y[a] == str(anno):
            pos += a

    ms = 0
    o_l = []
    for i in range(len(obj)):
        sells = int(obj[i][pos])
        if sells>ms:
            ms = sells
            i_ms = str(obj[i][0])
        elif sells==ms:
            ms = sells
            o_l.append(str(obj[i][0]))
            o_l.sort()
            i_ms = str(o_l[0])
    
    return i_ms
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
