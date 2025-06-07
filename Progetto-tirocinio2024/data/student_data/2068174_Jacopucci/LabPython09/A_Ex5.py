def A_Ex5(filename,oggetto):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f = open(filename,encoding="UTF-8")
    a = f.readline()
    v = a.strip().split(',')
    anni = []
    for i in range(1,len(v)):
        anni.append(v[i])
    for i in f:
        x = i.strip().split(',')
        if x[0]==oggetto:
            diff = 0
            anno = 1
            for j in range(2,len(x)):
                if int(x[j])-int(x[j-1])>=diff:
                    diff = int(x[j])-int(x[j-1])
                    anno = j
    f.close()
    return int(anni[anno-1])
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
