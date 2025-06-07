def A_Ex3(l):
    insieme = set()

    for x in range(len(l)):
        l2 = []
        for y in range(len(l)):
            if len(l[x]) == len(l[y]):
                l2.append(l[y])
        if len(l2) > 1:
            for a in range(len(l2)-1):
                for b in range(a+1, len(l2)):
                    if l2[a] != l2[b]:
                        insieme.add((l2[a],l2[b]))
                        insieme.add((l2[b], l2[a]))
        
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
