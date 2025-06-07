def A_Ex6(filename):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f = open(filename, encoding="utf-8")
    anno = f.readline()
    anno = anno.strip().split(",")
    f1 = f.readlines()
    ind = 0
    max1 = 0
    for i in range(len(f1)):
        f1[i] = f1[i].strip().split(",")
    for i in range(1, len(anno)):
        count = 0
        for j in range(len(f1)):
            count += int(f1[j][i])
        if count>=max1:
            max1 = count
            ind = i
    f.close()
    return int(anno[ind])
 
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
