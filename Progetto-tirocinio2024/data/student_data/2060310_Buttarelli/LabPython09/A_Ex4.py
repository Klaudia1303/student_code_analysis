def A_Ex4(filename,anno):
    f = open(filename, encoding = "UTF-8")
    l = []
    massimo = 0
    articoloMassimo = ""
    for i in f:
        i = i.strip().split(",")
        l.append(i)
    for i in range(1, len(l[0])):
        if int(l[0][i]) == anno:
            for j in range(1, len(l)):
                if int(l[j][l[0].index(str(anno))]) > massimo:
                    massimo = int(l[j][l[0].index(str(anno))])
                    articoloMassimo = l[j][0]
    f.close()
    print(articoloMassimo)
    return articoloMassimo
     
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
