def A_Ex4(filename,anno):
    tex = open(filename,encoding="UTF-8")
    mex = tex.readline()
    inf = mex.strip().split(",")
    con = 0
    max = 0
    res = ''
    for e in range(len(inf)):
        if inf[e].isdecimal() and int(inf[e]) == anno:
            con = e
    for i in tex:
        o = i.strip().split(",")
        if int(o[con]) > max or (int(o[con]) == max and o[0] > res):
            max = int(o[con])
            res = o[0]
    tex.close()
    return res
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
