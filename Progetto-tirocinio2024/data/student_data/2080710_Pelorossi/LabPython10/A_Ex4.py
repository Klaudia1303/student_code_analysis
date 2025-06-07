def A_Ex4(fileName):
    l=[]
    l2=[]
    d={}
    f=open(fileName,'r',encoding='UTF-8')
    for riga in f:
        l.append(riga.strip().split(','))

    l.remove(l[0])
    for elem in range(0,len(l)):
        if int(l[elem][1])>=18:
            l2.append(l[elem][0])

    for mat in range(len(l2)):
        d[int(l2[mat])]=int(l2.count(l2[mat]))
    return d
    
    




    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################


"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, ["esami1.csv"] , {1345: 1, 1346: 1, 1896: 1, 1753: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami2.csv"] , {1346: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami3.csv"] , {1347: 2, 1348: 1, 1349: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami4.csv"] , {1100: 1, 1012: 1, 1021: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami5.csv"] , {1345: 1, 1987: 1, 1346: 1, 1896: 1})

    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
