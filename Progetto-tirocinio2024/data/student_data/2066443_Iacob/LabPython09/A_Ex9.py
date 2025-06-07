def A_Ex9(fileName,squadra):
    o = open(fileName, 'r', encoding='UTF-8')
    r = o.read().split('\n')
    o.close()
    points = 0
    for p in range(1,len(r)):
        t = r[p].split(',')
        for gol in range(2):
            if t!=[''] and t[gol]==squadra:
                if int(t[gol+2])>int(t[3-gol]):
                    points += 3
                elif int(t[gol+2])==int(t[3-gol]):
                    points += 1
    return points
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
