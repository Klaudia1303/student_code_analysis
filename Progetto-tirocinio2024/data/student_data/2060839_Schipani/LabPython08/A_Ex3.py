def A_Ex3(l):
    coppia=()
    coppia2=()
    insieme=set()
    a=0
    j=1
    for i in l:
        a=j
        while a<len(l):
            if len(i)==len(l[a])and i!=l[a]:
                coppia=(i,l[a])
                coppia2=(l[a],i)
                insieme.add(tuple(coppia))
                insieme.add(tuple(coppia2))
            a+=1   
        j+=1
    return insieme

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, [['jkl', 'h', 'plqa', 'a', 'xkj']] , {('jkl','xkj'), ('h','a'), ('a','h'), ('xkj','jkl')})
    counter_test_positivi += tester_fun(A_Ex3, [[]] , set())
    counter_test_positivi += tester_fun(A_Ex3, [['a', 'ab', 'abc']] , set())
    counter_test_positivi += tester_fun(A_Ex3, [['e', 'a', 'lp', 'ql', 'cl']] ,  {('e', 'a'), ('a', 'e'), ('lp', 'ql'), ('lp', 'cl'), ('ql', 'lp'), ('ql', 'cl'), ('cl', 'lp'), ('cl', 'ql')})
    counter_test_positivi += tester_fun(A_Ex3, [['hjkl', 'hjkp']] , {('hjkl', 'hjkp'), ('hjkp', 'hjkl')} )


    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
