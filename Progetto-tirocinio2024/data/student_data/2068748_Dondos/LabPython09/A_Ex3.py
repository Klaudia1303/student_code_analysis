def A_Ex3(fileName):
    f = open(fileName, "r", encoding="UTF-8")
    f.readline()
    materie29 = set()
    ris = set()
    for riga in f:
        l = riga.strip().split(",")
        voto = int(l[1])
        materia = l[2].strip()
        if voto>=29:
            if materia in materie29:
                ris.add(materia)
            else:
                materie29.add(materia)
    f.close()
    return ris

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
