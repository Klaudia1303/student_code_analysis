def A_Ex3(fileName):
    f = open(fileName, encoding = "UTF-8")
    l = []
    insieme = set()
    for i in f:
        i = i.strip().split(",")
        l.append(i)
    for i in range(1, len(l)):
        contatore = 0
        for j in range(1, len(l)):
            if l[i][2] == l[j][2] and int(l[i][1]) >= 29:
                contatore += 1
        if contatore >= 2:
            insieme.add(l[i][2])
    f.close()
    return insieme

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
