def A_Ex3(fileName):
    l = []
    f = open(fileName, 'r', encoding="UTF-8")
    t = f.read().split('\n')
    f.close()

    for i in range(1, len(t)):
        s = t[i].split(',')
        if (s != [''] and int(s[1]) >= 29):
            l.append(s[2])
    l1 = []
    for i in range(len(l)):
        if (l.count(l[i]) >= 2):
            l1.append(l[i])
    return set(l1)

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
