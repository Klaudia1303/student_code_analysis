def A_Ex6(fileName):
    f=open(fileName,'r',encoding="UTF-8")
    u=f.readlines()
    d={}
    a=0
    p=set()
    for riga1 in u:
        a+=1
        x=riga1.strip().split(',')
        for i in range(len(x)):
            z=x[i]
            t=int(z)
            for riga2 in u:
                y=riga2.strip().split(',')
                k=d.keys()
                if (t not in k) and (z in y):
                    p.add(a)
                    d[t]=p
                elif (t in k) and (z in y):
                    q=d[t]
                    p.add(a)
                    r=q|p
                    d[t]=r
            p=set()
    f.close()
    return d
                



    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, ['numeri1.txt'] , {10: {1,2}, -5: {1,2}, 0: {1}, 8: {2}, -3: {2}})
    counter_test_positivi += tester_fun(A_Ex6, ['numeri2.txt'] , {10: {1,2}, 0: {2}})
    counter_test_positivi += tester_fun(A_Ex6, ['numeri3.txt'] , {3: {1,2}, 4: {1}, 5: {1}, 2: {2,3}, 0: {2,3}})
    counter_test_positivi += tester_fun(A_Ex6, ['numeri4.txt'] , {2: {1,2,3,4,5}, 1: {1,2,6}, 3: {6}})
    counter_test_positivi += tester_fun(A_Ex6, ['numeri5.txt'] , {})

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
