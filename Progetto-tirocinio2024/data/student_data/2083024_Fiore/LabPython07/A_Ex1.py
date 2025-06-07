def A_Ex1(l1, l2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    lista = []
    if len(l1) < len(l2):
        for i in range(len(l2)-len(l1)):
            l1.append(0)
    for v in range(len(l2)):
                   somma = l1[v] +l2[v]
                   lista.append(somma)
    return lista

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex1, [[3,6],[3,4,9]] , [6, 10, 9])
    counter_test_positivi += tester_fun(A_Ex1, [[],[3,4,9]] , [3, 4, 9])
    counter_test_positivi += tester_fun(A_Ex1, [[3,6],[3,4]] ,[6, 10])
    counter_test_positivi += tester_fun(A_Ex1, [[1],[9]] ,[10])
    counter_test_positivi += tester_fun(A_Ex1, [[],[9]] ,[9])

    print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
