def A_Ex3(fileName):
    f = open(fileName, encoding = "UTF-8")
    l = []
    for elem in f:
        elem = elem.strip().split(",")
        l.append(elem)
    f.close()
    materia = []
    for elem in l:
        if elem[1].isnumeric() and int(elem[1]) >= 29:
            materia.append(elem[-1])
    insieme1 = set()
    for i in range(len(materia)):
        conto = materia.count(materia[i])
        if conto > 1 :
            insieme1.add(materia[i])
    return(insieme1)
            
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
