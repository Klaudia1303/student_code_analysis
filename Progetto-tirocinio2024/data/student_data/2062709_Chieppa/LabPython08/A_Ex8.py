def A_Ex8(l):
    insieme=set()
    lista=[]
    for i in l:
        if l.count(i)==1:
            lista.append(i)
    l=lista
    for i in l:
        for n in i:
            ok=True
            for j in l:
                if j!=i and n in j:
                    ok=False
            if ok:
                insieme.add(n)
    return insieme


    

    
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
