def A_Ex8(file):
    f = open(file, "r", encoding="UTF-8")

    riga = f.readline()

    d = {}

    while len(riga) > 0:
        riga = f.readline()
        elem = riga.strip().split(",")

        if len(elem) > 1: 
            for x in range(2):
                oth = abs(x-1)
                if elem[x] in d:
                    if elem[2] == "amici" and d[elem[x]].count(elem[oth]) == 0:
                        d[elem[x]].append(elem[oth])
                        d[elem[x]].sort()
                    elif elem[2] == "nemici" and d[elem[x]].count(elem[oth]) == 1:
                        d[elem[x]].remove(elem[oth])
                else:
                    if elem[2] == "amici":
                        d[elem[x]] = [elem[oth]]

    f.close()

    return d 


    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex8, ["amici1.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna'], 'Giorgio': []})
    counter_test_positivi += tester_fun(A_Ex8, ["amici2.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria'], 'Maria': ['Anna'], 'Paola': [], 'Giorgio': []})
    counter_test_positivi += tester_fun(A_Ex8, ["amici3.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna'], 'Giorgio': []})
    counter_test_positivi += tester_fun(A_Ex8, ["amici4.csv"] , {'Marco': ['Giorgio', 'Paolo'], 'Giorgio': ['Marco'], 'Paolo': ['Marco'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna']})
    counter_test_positivi += tester_fun(A_Ex8, ["amici5.csv"] , {'Marco': [], 'Giorgio': [], 'Paola': [], 'Anna': []})

    print('La funzione',A_Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
