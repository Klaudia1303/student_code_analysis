def A_Ex8(l):
    a=0
    conta=0
    b=0
    i1=set()
    casa=True
    while a<len(l):
        for i in l[a]:
            while casa:
                if i in l[b]:
                    conta+=1
                b+=1
                if b==len(l):
                    casa=False
            if conta==1:
                i1.add(i)
            casa=True
            b=0
            conta=0
        a+=1
    return(i1)
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

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
