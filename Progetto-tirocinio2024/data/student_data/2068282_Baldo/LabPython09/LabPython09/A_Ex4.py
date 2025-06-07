def A_Ex4(filename,anno):
    f = open(filename)
    s = f.readlines()
    l = []

    for riga in s:
        l.append(riga.strip().split(","))

    obj = ""
    sell = 0

    for i in l[1:]:
        if int(i[l[0].index(str(anno))]) > sell:
            obj = i[0]
            sell = int(i[l[0].index(str(anno))])
        elif int(i[l[0].index(str(anno))]) > sell:
            if i[0] > obj:
                obj = i[0]
                sell = int(i[l[0].index(str(anno))])
    f.close()
    return obj
                 
        
        
     
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
