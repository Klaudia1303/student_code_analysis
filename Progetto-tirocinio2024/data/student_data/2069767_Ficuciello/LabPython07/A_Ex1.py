def A_Ex1(l1, l2):
    l3=[]

    if len(l1)==len(l2):
        for e1 in l1:
            for e2 in l2:
                c=e1+e2
                l3.append(c)
    if len(l1)<len(l2):
        for e2 in l2:
            c=0+e2
            l3.append(c)
    if len(l1)>len(l2):
        for e1 in l1:
            c=e1+0
            l3.append(c)
                
    return(l3)
            


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex1, [[3,6],[3,4,9]] , [6, 10, 9])
    counter_test_positivi += tester_fun(A_Ex1, [[],[3,4,9]] , [3, 4, 9])
    counter_test_positivi += tester_fun(A_Ex1, [[3,6],[3,4]] ,[6, 10])
    counter_test_positivi += tester_fun(A_Ex1, [[1],[9]] ,[10])
    counter_test_positivi += tester_fun(A_Ex1, [[],[9]] ,[9])

    print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
