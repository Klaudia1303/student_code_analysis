from tester import tester_fun

def A_Ex4(l):
    ins=set()
    for i in range (len(l)):
        parola=l[i]
        for j in range (len(l)):
            if len(parola)==len(l[j]) and parola!=l[j]:
                tupla=(parola,l[j])
                ins.add(tupla)
    return ins


###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, [['jkl', 'h', 'plqa', 'a', 'xkj']] , {('jkl','xkj'), ('h','a'), ('a','h'), ('xkj','jkl')})
    counter_test_positivi += tester_fun(A_Ex4, [[]] , set())
    counter_test_positivi += tester_fun(A_Ex4, [['a', 'ab', 'abc']] , set())
    counter_test_positivi += tester_fun(A_Ex4, [['e', 'a', 'lp', 'ql', 'cl']] ,  {('e', 'a'), ('a', 'e'), ('lp', 'ql'), ('lp', 'cl'), ('ql', 'lp'), ('ql', 'cl'), ('cl', 'lp'), ('cl', 'ql')})
    counter_test_positivi += tester_fun(A_Ex4, [['hjkl', 'hjkp']] , {('hjkl', 'hjkp'), ('hjkp', 'hjkl')} )


    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
