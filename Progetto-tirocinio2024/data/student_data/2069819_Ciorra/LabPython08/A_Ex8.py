from tester import tester_fun

def A_Ex8(l):
    r=set()
    # rimozione doppioni
    l2 = []
    for i in l:
        if l.count(i) == 1:
            l2.append(i)
    l = l2
    ####################
    for i in l:
        for elem in i:
            prendo=True
            for i2 in l:
                if i2!=i and elem in i2:
                    prendo=False
            if prendo:
                r.add(elem)
    return r

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

    counter_test_positivi += tester_fun(A_Ex8, [[{10}]] , {10})
    counter_test_positivi += tester_fun(A_Ex8, [[{10,2}]] , {10,2})
    counter_test_positivi += tester_fun(A_Ex8, [[{10,2},{10}]] , {2})
    counter_test_positivi += tester_fun(A_Ex8, [[{1},{1},{1}]] , set())
    counter_test_positivi += tester_fun(A_Ex8, [[{6},{1},{1,2,3,4,5,6}]] , {2,3,4,5})


    print('La funzione',A_Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
