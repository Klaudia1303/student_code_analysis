def A_Ex1(l1, l2):
    s=0
    vuoto=[]
    somma=[]
    listavalori1=[]
    listavalori2=[]
    if(len(l1)==0 and len(l2)==0):
        return vuoto
        
    for i in range(len(l1)):
            v_l1=l1[i]
            v_l2=l2[i]
            s=v_l1+v_l2
            somma.append(s)
            listavalori1.append(v_l1)
            listavalori2.append(v_l2)

    for j in l2:
        if j not in listavalori2 and j not in listavalori1:
                somma.append(j)
                     
    return somma
        
    
        

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
