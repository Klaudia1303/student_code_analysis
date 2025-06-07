def A_Ex2(l):
    lf=set()
    for i in l:
        i="".join(sorted(i))
        while (len(i)>0):
            if(i.count(i[0])>1):
                t=i[0]
                lf.add(i[0])
                while (i.count(t)>0):
                    i=i[1:len(i)]
                continue
            i=i[1:len(i)]
    return(lf)

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex2, [['casa', 'albero', 'bello']] , {'a','l'})
    counter_test_positivi += tester_fun(A_Ex2, [['ciao', 'ciao']] , set())
    counter_test_positivi += tester_fun(A_Ex2, [['aa','aa','hghjklhl']] , {'a','h','l'})
    counter_test_positivi += tester_fun(A_Ex2, [[]] , set())
    counter_test_positivi += tester_fun(A_Ex2, [['cogito', 'ergo', 'sum']] , {'o'})


    print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
