def A_Ex6(filename):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(filename,'r', encoding="UTF-8")
    a=f.readline()
    f.close()
    a = a.strip().split(',')[1:]
    Max = 0
    anno = 0
    i = 0
    while i < len(a):
        f=open(filename,'r', encoding="UTF-8")
        somma = 0
        for q in f:
            if 'Anno' in q:
                continue
            q = q.strip().split(',')[1:]
            somma = somma + int(q[i])
        f.close()
        if somma >= Max:
            Max = somma
            anno = int(a[i])
        i += 1
    return anno
            
        
 
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
