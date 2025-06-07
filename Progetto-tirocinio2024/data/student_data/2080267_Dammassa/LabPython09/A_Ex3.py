def A_Ex3(fileName):
    f = open(fileName, encoding="UTF-8")
    l = []
    l1 = []
    l2 = []
    for elem in f:
        elem = elem.strip().split(",")
        l1.append(elem)
    for i in range(1, len(l1)):
        if int(l1[i][1])>=29:
            l2.append((l1[i][2]))
            for j in range(len(l2)):
                if l2.count(l2[j])>=2:
                    l.append(l2[j])
    f.close()
    return set(l)
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
