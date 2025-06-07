def A_Ex4(l):
    l2=l.copy()
    a=0
    k=0
    risultato=set()
    for i in l2:
        a=l.count(i)
        b=(i,a)
        if a>0:
            risultato.add(b)
        while k<l.count(i):
            l.remove(i)
    return(risultato)
        

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, [['jkl', 'h', 'plqa', 'jkl', 'h', 'xkj']] , {('jkl',2), ('h',2), ('plqa',1), ('xkj',1)})
    counter_test_positivi += tester_fun(A_Ex4, [[]] , set())
    counter_test_positivi += tester_fun(A_Ex4, [['a', 'ab', 'abc']] , {('a', 1), ('ab', 1), ('abc', 1)})
    counter_test_positivi += tester_fun(A_Ex4, [['e', 'a', 'e', 'lp', 'a', 'ql', 'cl']] ,  {('e', 2), ('a', 2), ('lp', 1), ('ql', 1), ('cl', 1)} )
    counter_test_positivi += tester_fun(A_Ex4, [['hjkl', 'hjkl']] , {('hjkl', 2)})


    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

