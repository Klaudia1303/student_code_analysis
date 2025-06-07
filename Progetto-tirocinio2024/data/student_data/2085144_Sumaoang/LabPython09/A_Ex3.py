def A_Ex3(fileName):
    primo = set()
    secondo = set()
    f = open(fileName, encoding="UTF-8")
    f.readline()
    for x in f:
        esame1 = x.strip()
        esame2 = esame1.split(",")
        if int(esame2[1]) >= 29:
            if not esame2[2] in primo:
                primo.add(esame2[2])
            else:
                secondo.add(esame2[2])
    return secondo
        
        

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
