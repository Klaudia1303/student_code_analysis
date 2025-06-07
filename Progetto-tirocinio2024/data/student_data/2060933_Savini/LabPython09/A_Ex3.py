def A_Ex3(fileName):
    f= open(fileName, encoding="UTF-8")
    i=set()
    f.readline()
    p=f.readlines()
    for c in p:
        a= c.strip().split(',')
        for j in p:
            b=j.strip().split(',')
            if a[0]!=b[0]:
                if int(a[1])>=29 and int(b[1])>=29:
                    if a[2] == b[2]:
                        i.add(b[2])
    f.close()
    return i



    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun
    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"], {'Fisica'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"], set())
    counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"], {'Ricerca Operativa','Analisi'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"], {'Basi di Dati'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"], set())

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
