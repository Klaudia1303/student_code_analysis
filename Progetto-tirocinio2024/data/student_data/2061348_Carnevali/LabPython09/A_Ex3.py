def A_Ex3(fileName):
    a=open(fileName)
    b=a.readlines()
    c=set()
    for n in range(1,len(b)):
        d=b[n].strip().split(",")
        if int(d[1])>=29:
            for m in range(1,len(b)):
                e=b[m].strip().split(",")
                if int(e[1])>=29 and e[2]==d[2] and d[2]not in c and d[0]!=e[0]:
                    c.add(e[2])
    return c
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
