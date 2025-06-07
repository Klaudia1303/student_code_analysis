def A_Ex3(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f = open(fileName)
    r = f.readlines()
    materie = set()
    for i in range(1, len(r)):
        conta = 0
        stringa = r[i].split(",")
        temp_materia = stringa[2].strip()
        for k in range(1, len(r)):
            stringa2 = r[k].split(",")
            materia2 = stringa2[2].strip()
            if materia2 == temp_materia:
                if int(stringa2[1]) > 28:
                    conta = conta + 1
            if conta > 1:
                materie.add(temp_materia)
                break
    return(materie)
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
