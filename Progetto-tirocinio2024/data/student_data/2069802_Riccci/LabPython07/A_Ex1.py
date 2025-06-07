def A_Ex1(l1, l2):
    i=0
    l3=[]
    if len(l2)==len(l1):
        for i in range(len(l1)):
            l3.append(l1[i]+l2[i])
        return l3
    elif len(l2)>len(l1):
        for i in range(len(l1)):
            l3.append(l1[i]+l2[i])
        for j in range(i+1,len(l2)):
            l3.append(l2[j])
        return l3
    else:
        return l3
            
            

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
