def A_Ex3(fileName):
    f = open(fileName, encoding = "UTF-8")
    insieme = set()
    f.readline()
    l = f.readlines()
    for riga1 in l:
        a = riga1.strip().split(",")
        for riga2 in l:
            b = riga2.strip().split(",")
            if a != b:
                if int(a[1]) >= 29 and int(b[1]) >= 29:
                    if a[2] == b[2]:
                        insieme.add(a[2])
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
