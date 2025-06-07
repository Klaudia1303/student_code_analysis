def A_Ex6(fileName):
    file = open (fileName, encoding = 'UTF-8')
    l = []
    for elem in file :
        elem = elem.strip().split(',')
        l.append(elem)
    d = {}
    for i in range(len(l)):
        riga = l[i]
        for num in riga:
            insieme = set()
            if int(num) not in d :
                insieme.add(i+1)
                d[int(num)] = insieme
            else:
                insieme.add(i+1)
                d[int(num)] = d[int(num)] | insieme
    return (d)


 
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
