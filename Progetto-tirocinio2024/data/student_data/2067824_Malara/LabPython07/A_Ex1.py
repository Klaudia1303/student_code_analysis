def A_Ex1(l1, l2):
    
    if l1==[]:
        return l2
    else:
        lsomma=[]
        for i in range(len(l1)):
            somma=l1[i]+l2[i]
            lsomma.append(somma)
        if len(l1)<len(l2):
            c=1
            while c<=len(l2)-len(l1):
                somma=l2[i+c]
                lsomma.append(somma)
                c+=1
        
    return lsomma

    
        

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
