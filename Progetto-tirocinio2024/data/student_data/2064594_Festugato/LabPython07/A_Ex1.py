def A_Ex1(l1, l2):
    
    somma = 0
    l_somma = []
    valori_considerati1 = []
    valori_considerati2 = []

    if l1==[] and l2==[]:
        l.somma = []
        
    
    else :
        for i in range(len(l1)):
            valore1 = l1[i]
            valore2 = l2[i]
            valori_considerati1.append(valore1)
            valori_considerati2.append(valore2)
            
        
            somma = valore1 + valore2
            l_somma.append(somma)
            
        
    #valori non inseriti
    for n in l2 :
        if n not in valori_considerati1 and n not in valori_considerati2:
            l_somma.append(n)

    return l_somma
    

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
