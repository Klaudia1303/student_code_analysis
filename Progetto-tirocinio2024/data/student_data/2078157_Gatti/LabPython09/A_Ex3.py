def A_Ex3(fileName):
    f = open(fileName, encoding = 'UTF-8')
    f.readline()
    A = set()
    s = f.readlines()
    l1 = []
    for riga in s:
        l = riga.strip().split(',')
        if int(l[1]) >= 29:
            l1.append(l[2])
    for elem in l1:
        if l1.count(elem) >= 2:
            A.add(elem)
        
                
    f.close()
    return A
            

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun
    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"], {'Fisica'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"], set())
    counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"], {'Ricerca Operativa','Analisi'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"], {'Basi di Dati'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"], set())

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
