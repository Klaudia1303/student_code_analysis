from tester import tester_fun

def A_Ex4(l):
    r=set()
    for elem1 in l:
        cont=0
        for elem2 in l:
            if elem1==elem2:
                cont=cont+1
        r.add((elem1,cont))
    return r

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(A_Ex4, [['jkl', 'h', 'plqa', 'jkl', 'h', 'xkj']] , {('jkl',2), ('h',2), ('plqa',1), ('xkj',1)})
    counter_test_positivi += tester_fun(A_Ex4, [[]] , set())
    counter_test_positivi += tester_fun(A_Ex4, [['a', 'ab', 'abc']] , {('a', 1), ('ab', 1), ('abc', 1)})
    counter_test_positivi += tester_fun(A_Ex4, [['e', 'a', 'e', 'lp', 'a', 'ql', 'cl']] ,  {('e', 2), ('a', 2), ('lp', 1), ('ql', 1), ('cl', 1)} )
    counter_test_positivi += tester_fun(A_Ex4, [['hjkl', 'hjkl']] , {('hjkl', 2)})

    counter_test_positivi += tester_fun(A_Ex4, [['a', 'aa']] , {('a', 1), ('aa', 1)})
    counter_test_positivi += tester_fun(A_Ex4, [['a', 'a','a']] , {('a', 3)})
    counter_test_positivi += tester_fun(A_Ex4, [['','a','']] , {('a', 1), ('',2)})
    counter_test_positivi += tester_fun(A_Ex4, [['a','b','a','b','a']] , {('a', 3), ('b',2)})
    counter_test_positivi += tester_fun(A_Ex4, [['AAA','BBB','AAA']] , {('AAA', 2), ('BBB',1)})

    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

