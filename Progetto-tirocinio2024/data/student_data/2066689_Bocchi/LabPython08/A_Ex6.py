def A_Ex6(l,c,n):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    l2=l.copy()
    if l == 0:
        l= []
    for el in l2:
        #print('elemento', el)
        for i in range(len(el)):
            #print('i', i)
            if el[i]==c and el.count(el[i])>= n:
                #print('elimina1',el)
                l.remove(el)
                break
    return l

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, [['palla','casse','palo'],'a',2] ,['casse','palo'])
    counter_test_positivi += tester_fun(A_Ex6, [['palla','casse','palo'],'p',1] ,['casse'])
    counter_test_positivi += tester_fun(A_Ex6, [['pallone','casse','palla','pappa'],'p',2] ,['pallone','casse','palla'])
    counter_test_positivi += tester_fun(A_Ex6, [['pallone','casse','palla','pappa'],'a',1], [])
    counter_test_positivi += tester_fun(A_Ex6, [[],'a',1] , [])


    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
