def A_Ex5(filename,oggetto):
    f = open(filename, encoding = "UTF-8")
    l = []
    massimo = 0
    annoMassimo = 0
    for i in f:
        i = i.strip().split(",")
        l.append(i)
    for i in range(1, len(l)):
        if l[i][0] == oggetto:
            for j in range(1, len(l[i])):
                if int(l[i][j]) > massimo:
                    massimo = int(l[i][j])
                    annoMassimo = int(l[0][l[i].index(l[i][j])])
    f.close()
    return annoMassimo

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
