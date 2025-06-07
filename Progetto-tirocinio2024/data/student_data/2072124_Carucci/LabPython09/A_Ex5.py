def A_Ex5(filename,oggetto):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    anno = 0
    f = open(filename, encoding="UTF-8")
    a= f.readline()
    a = a.strip().split(',')
    anno = int(a[1])
    for r in f:
        r = r.strip().split(',')
        if r[0] == oggetto:
            maxca = 0
            for x in range(1, len(r)-1):
                ca = int(r[x+1])-int(r[x])
                if ca > maxca or (ca == maxca and int(a[x+1])>anno):
                    maxca = ca
                    anno = int(a[x+1])
                
            break
    f.close()

    return anno
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Giubbotto'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Zaino'] , 2010)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Maglione'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Zaino'] , 2013)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite3.csv','Giubbotto'] , 2013)

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
