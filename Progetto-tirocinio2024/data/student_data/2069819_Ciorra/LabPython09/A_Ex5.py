def A_Ex5(filename,oggetto):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f = open(filename, encoding="utf-8")
    m = 0
    for g in f:
        g = g.strip().split(",")
        break
    for i in f:
        i= i.strip().split(",")
        if i[0] == oggetto:
            x = i
    for c in range(1, len(x) -1):
        z = int(x[c+1])-int(x[c])
        if z>=m:
            m = z
            sa = c+1
        elif m==0:
            sa = 1
    return int(g[sa])
        
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

