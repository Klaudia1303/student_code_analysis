def A_Ex6(l1, l2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    var=False
    lista=[]
    controllo=0

    if len(l1)>len(l2):
        for i in range(len(l1)):
            controllo=l1[i]
            var=False
            for x in range(len(l2)):
                if var==False:
                    if controllo==l2[x]:
                        var=True
                    else:
                        var=False
            if var==False:
                lista.append(controllo)              
    lista.sort()
    return lista
    

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, [[1, 3, 2, 1, -5],[1, 3]],[-5, 2])
    counter_test_positivi += tester_fun(A_Ex6, [[1, 3, 2, 1, -5],[1, 1, 1]],[-5, 2, 3])
    counter_test_positivi += tester_fun(A_Ex6, [[10, 1, 10, 1, 2],[10, 1, 2]],[])
    counter_test_positivi += tester_fun(A_Ex6, [[],[1, 1, 1]],[])
    counter_test_positivi += tester_fun(A_Ex6, [[100, 12, -2, -1, -2],[]],[-2, -2, -1, 12, 100])

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
