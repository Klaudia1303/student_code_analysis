def A_Ex6(l,c,n):
    lr=[]
    for i in l:
        if i.count(c) < n:
            lr.append(i)
    return lr
            
            

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
