def A_Ex1(l1, l2):
    if l1==l2==[]:
        l3=[]
        
    elif len(l2)>len(l1):
        l3=[0 for i in range (len(l2))]
        while len(l2)!=len(l1):
            l1.append(0)
        for i in range(len(l2)):
            l3[i]=l2[i]+l1[i]

    elif len(l2)==len(l1):
        l3=[0 for i in range (len(l2))]
        for i in range(len(l2)):
            l3[i]=l2[i]+l1[i]
            
    elif len(l1)>len(l2):
        l3=[0 for i in range (len(l1))]
        while len(l2)!=len(l1):
            l2.append(0)
        for i in range(len(l2)):
            l3[i]=l2[i]+l1[i] 
        
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
