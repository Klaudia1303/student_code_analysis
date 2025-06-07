def A_Ex6(filename):
    f = open(filename, "r", encoding="UTF-8")
    t = f.read().split('\n')
    f.close()
    m = 0
    a = 0
    for i in range(1, len(t[0].split(','))):
        ml = 0
        for j in range(1, len(t)):
            ml += int(t[j].split(',')[i])
        if (ml > m):
            m = ml
            a = int(t[0].split(',')[i])
        elif (ml == m):
            a = max(a, int(t[0].split(',')[i]))
    return a
    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, ['Vendite1.csv'] , 2010)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite2.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite3.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite4.csv'] , 2020)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite5.csv'] , 2022)

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
