def A_Ex3(fileName):
    f = open (fileName, "r", encoding = "UTF-8")
    s = f.readline()
    ris = []
    insieme = set()
    for riga in f:
        riga = riga.strip().split(",")
        if int(riga[1]) >= 29:
            ris.append(riga)
    for i in range (0, len(ris)):
        materia = ris[i][2]
        somma = 0
        for j in range (0, len(ris)):
            if ris[j][2] == materia:
                somma = somma + 1
                if somma >= 2:
                    insieme.add(materia)
    f.close()
    return insieme
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
