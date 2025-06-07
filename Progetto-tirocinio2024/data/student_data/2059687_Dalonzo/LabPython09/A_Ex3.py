def A_Ex3(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    file = open(fileName,'r', encoding='UTF-8')
    materie = set()
    file.readline()
    for riga in file:
        val = riga.strip().split(',')
        materia = val[2]
        count = 0
        file2 = open(fileName,'r', encoding='UTF-8')
        file2.readline()
        for riga in file2:
            val2 = riga.strip().split(',')
            if(val2[2] == materia and int(val2[1]) >= 29):
                count += 1
            if(count >= 2):
                materie.add(val2[2])
                count = 0
                break

    return materie
            
            
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
