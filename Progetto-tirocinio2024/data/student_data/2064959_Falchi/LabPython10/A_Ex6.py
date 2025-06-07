def A_Ex6(fileName):
    d = dict()
    rigaCorrente = 1

    with open(fileName, "r", encoding="UTF-8") as file:
        rigaNonFormattata = file.readline()

        while len(rigaNonFormattata) > 0:
            riga = rigaNonFormattata.strip().split(",")
                
            print("La riga:", rigaNonFormattata,riga)

            for valore in riga:
                print("valore", valore)
                if not int(valore) in d:
                    d[int(valore)] = set()

                print("riga", rigaCorrente)
                d[int(valore)].add(rigaCorrente)
                
            rigaNonFormattata = file.readline()
            rigaCorrente += 1
    return d
    
 
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
