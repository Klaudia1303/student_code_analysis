def A_Ex3(fileName):
    f = open(fileName, encoding = "UTF-8")
    l = set()
    for i in f:
        i = i.split(",")
        cont = 0
        f1 = open(fileName, encoding = "UTF-8")
        for j in f1:
            j = j.split(",")
            if(j[1] != "Voto" and i[1] != "Voto" and int(j[1]) >= 29 and int(i[1]) >= 29 and j[2].strip() == i[2].strip()):
                cont += 1
        if (cont > 1):
            l.add(i[2].strip())
        f1.close()
    f.close()
    return(l)
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
