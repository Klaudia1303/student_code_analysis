def A_Ex7(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    if len(l)==0:
        return []
    a = l.copy()
    x = len(a)
    y = 0
    j = 0
    while j < 1:
        for i in range(y, x):
            if i == x-1:
                break
            if a[i]<a[i+1]:
                a.append(a[i+1]-a[i])
        if len(a) != x:
            y = x-1
            x = len(a)
        if i == x-1:
            j += 1
            
    return a
        
    
    

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
