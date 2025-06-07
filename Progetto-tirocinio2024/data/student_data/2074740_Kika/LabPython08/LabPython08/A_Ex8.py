def A_Ex8(l):
    #"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    k=[]
    v=set()
    for i in l:
        k=k+list(i)
    for j in k:
        if k.count(j)==1:
            v.add(j)
    return v

    
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex8, [[{3,2,90},{2,87,23},{2,23,3}]] , {90,87})
    counter_test_positivi += tester_fun(A_Ex8, [[set(),{-10},{2}]] , {-10,2})
    counter_test_positivi += tester_fun(A_Ex8, [[set()]] , set())
    counter_test_positivi += tester_fun(A_Ex8, [[set(),{10,-2},{10},{-2}]] , set())
    counter_test_positivi += tester_fun(A_Ex8, [[set(),{10,-9,4},{4,-5,2},{3,7,4}]] , {10,-9,-5,2,3,7})


    print('La funzione',A_Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
