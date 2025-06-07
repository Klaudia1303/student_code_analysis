def A_Ex9(fileName,squadra):
    f = open(fileName, "r", encoding="UTF-8")
    elem = f.read().split('\n')
    punti = 0
    for i in range(1,len(elem)):
        elem2 = elem[i].split(',')
        for k in range(2):
            if (elem2 != [''] and elem2[k] == squadra):
                if (int(elem2[k+2]) > int(elem2[3-k])):
                    punti = punti+3
                elif (int(elem2[k+2]) == int(elem2[3-k])):
                    punti = punti+1
    return punti
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex9, ["partite1.csv",'Chelsea'] , 3)
    counter_test_positivi += tester_fun(A_Ex9, ["partite1.csv",'Tottenham'] , 1)
    counter_test_positivi += tester_fun(A_Ex9, ["partite2.csv",'Arsenal'] , 4)
    counter_test_positivi += tester_fun(A_Ex9, ["partite2.csv",'Bayern'] , 0)
    counter_test_positivi += tester_fun(A_Ex9, ["partite3.csv",'Bayern'] , 4)

    print('La funzione',A_Ex9.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
