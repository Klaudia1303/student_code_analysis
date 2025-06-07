def A_Ex3(fileName):
    mat = set()
    l = []
    gg = []
    o = open(fileName, encoding='UTF-8')
    for line in o:
        line = line.strip().split(',')
        l.append(line)
    for el in range(1,len(l)):
        if int(l[el][1])>=29:
            gg.append(l[el][2])
    gg.sort()
    for s in range(len(gg)-1):
        if gg[s]==gg[s+1]:
            mat.add(gg[s])
    return mat
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
