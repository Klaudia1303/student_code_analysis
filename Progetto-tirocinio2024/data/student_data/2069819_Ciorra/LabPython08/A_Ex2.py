from tester import tester_fun

def A_Ex2(l):
    r=set()
    for s in l:
        for c in s:
            if s.count(c)>1:
                r.add(c)
    return r

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(A_Ex2, [['casa', 'albero', 'bello']] , {'a','l'})
    counter_test_positivi += tester_fun(A_Ex2, [['ciao', 'ciao']] , set())
    counter_test_positivi += tester_fun(A_Ex2, [['aa','aa','hghjklhl']] , {'a','h','l'})
    counter_test_positivi += tester_fun(A_Ex2, [[]] , set())
    counter_test_positivi += tester_fun(A_Ex2, [['cogito', 'ergo', 'sum']] , {'o'})

    counter_test_positivi += tester_fun(A_Ex2, [['Aa', 'Aa', 'Aa']] , set())
    counter_test_positivi += tester_fun(A_Ex2, [['ZaZ', 'abca']] , {'Z','a'})
    counter_test_positivi += tester_fun(A_Ex2, [['1111111', '12345678']] , {'1'})
    counter_test_positivi += tester_fun(A_Ex2, [['abCdEfF', 'qwertya','g_g','zz','ZZ']] , {'g','z','Z'})
    counter_test_positivi += tester_fun(A_Ex2, [['a', 'a','aa']] , {'a'})


    print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
