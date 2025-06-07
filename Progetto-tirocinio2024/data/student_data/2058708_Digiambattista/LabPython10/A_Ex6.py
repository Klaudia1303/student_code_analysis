def A_Ex6(fileName):
    f = open(fileName)
    r = f.readlines()
    dizionario = {}
    insieme = set()
    for n in range(len(r)):
        r[n] = r[n].strip().split(",")
        for k in r[n]:
            insieme.add(n + 1)
            if int(k) not in dizionario.keys(): 
                dizionario.update({int(k):insieme})
            else:
                dizionario[int(k)] = dizionario[int(k)].union({n + 1})
            insieme = set()
    return dizionario
        
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
