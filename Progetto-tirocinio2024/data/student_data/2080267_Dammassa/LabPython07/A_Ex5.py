def A_Ex5(l):
    n1 = 0
    n = 0
    l1 = []
    i = 0
    if l == []:
         return l
    for i in range(len(l)):
        k = l[i]
        for j in range(len(k)):
            print(j, len(k), i)
            n = ord(k[j])
            n1 += n
            print(n1)
            i += 1
        l1.append(n1)
        n1 = 0
        i = 0
            
                
         
    return l1
       

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, [["ama","ma","amaca"]], [303,206,499])
    counter_test_positivi += tester_fun(A_Ex5, [[]], [])
    counter_test_positivi += tester_fun(A_Ex5, [["c"]], [99])
    counter_test_positivi += tester_fun(A_Ex5, [["ciao",""]], [412,0])
    counter_test_positivi += tester_fun(A_Ex5, [["",""]], [0,0])

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
