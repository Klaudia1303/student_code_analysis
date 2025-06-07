from tester import tester_fun

def A_Ex5(l):
        conta=0
        ins=set()
        for i in range (len(l)):
                parola=l[i]
                for j in range (len(l)):
                        if parola==l[j]:
                                conta+=1
                tupla=(parola,conta)
                ins.add(tupla)
                conta=0
        return ins
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, [['jkl', 'h', 'plqa', 'jkl', 'h', 'xkj']] , {('jkl',2), ('h',2), ('plqa',1), ('xkj',1)})
    counter_test_positivi += tester_fun(A_Ex5, [[]] , set())
    counter_test_positivi += tester_fun(A_Ex5, [['a', 'ab', 'abc']] , {('a', 1), ('ab', 1), ('abc', 1)})
    counter_test_positivi += tester_fun(A_Ex5, [['e', 'a', 'e', 'lp', 'a', 'ql', 'cl']] ,  {('e', 2), ('a', 2), ('lp', 1), ('ql', 1), ('cl', 1)} )
    counter_test_positivi += tester_fun(A_Ex5, [['hjkl', 'hjkl']] , {('hjkl', 2)})


    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

