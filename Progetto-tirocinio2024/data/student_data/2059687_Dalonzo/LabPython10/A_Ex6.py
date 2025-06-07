def A_Ex6(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    file = open(fileName,'r',encoding = 'UTF-8')
    diz = {}
     
    for riga in file:
        values = riga.strip().split(',')
        for value in values:
            value = int(value)
            if(value not in diz):
                index = 1
                file2 = open(fileName,'r',encoding = 'UTF-8')
                for riga2 in file2:
                    list_of_strings = riga2.strip().split(',')
                    nums = map(int, list_of_strings)
                    if(int(value) in nums):                        
                        if(value not in diz):
                             diz[value] = {index}
                        else:
                             diz[value].add(index)
                    index += 1
    file.close()
    return diz
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
