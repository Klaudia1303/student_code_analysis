from tester import tester_fun

def A_Ex3(l):
    r=set()
    for elem1 in l:
        for elem2 in l:
            if len(elem1)==len(elem2) and elem1!=elem2:
                r.add((elem1,elem2))
    return r

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(A_Ex3, [['jkl', 'h', 'plqa', 'a', 'xkj']] , {('jkl','xkj'), ('h','a'), ('a','h'), ('xkj','jkl')})
    counter_test_positivi += tester_fun(A_Ex3, [[]] , set())
    counter_test_positivi += tester_fun(A_Ex3, [['a', 'ab', 'abc']] , set())
    counter_test_positivi += tester_fun(A_Ex3, [['e', 'a', 'lp', 'ql', 'cl']] ,  {('e', 'a'), ('a', 'e'), ('lp', 'ql'), ('lp', 'cl'), ('ql', 'lp'), ('ql', 'cl'), ('cl', 'lp'), ('cl', 'ql')})
    counter_test_positivi += tester_fun(A_Ex3, [['hjkl', 'hjkp']] , {('hjkl', 'hjkp'), ('hjkp', 'hjkl')} )

    counter_test_positivi += tester_fun(A_Ex3, [['x', 'y']] , {('x', 'y'), ('y', 'x')} )
    counter_test_positivi += tester_fun(A_Ex3, [['Aa', 'Aa']] , set() )
    counter_test_positivi += tester_fun(A_Ex3, [['', '', 'A','B','C']] , {('A', 'B'), ('B', 'A'), ('A', 'C'), ('C', 'A'), ('B', 'C'), ('C', 'B')})
    counter_test_positivi += tester_fun(A_Ex3, [['A','AA','bcd']] , set())
    counter_test_positivi += tester_fun(A_Ex3, [['H','H']] , set())



    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

