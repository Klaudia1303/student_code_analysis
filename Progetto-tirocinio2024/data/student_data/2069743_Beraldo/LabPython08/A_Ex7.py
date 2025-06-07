def A_Ex7(l):
    x = len(l)
    i= 1
    while i < x:
        if l[i-1] < l[i]:
            l.append(l[i]-l[i-1])
            x+=1
        i+=1
    return l
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex7, [[10,1,11,31,251]] , [10,1,11,31,251,10,20,220,10,200,190])
    counter_test_positivi += tester_fun(A_Ex7, [[]] , [])
    counter_test_positivi += tester_fun(A_Ex7, [[2,7,3]] , [2,7,3,5,2])
    counter_test_positivi += tester_fun(A_Ex7, [[200,501,300]] , [200,501,300,301,1])
    counter_test_positivi += tester_fun(A_Ex7, [[3,2,0]] , [3,2,0])


    print('La funzione',A_Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
