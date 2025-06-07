def A_Ex8(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f = open(file,encoding="UTF-8")
    f.readline()
    d = {}
    for i in f:
        x = "".join(i.strip().split("\n"))
        xs = x.strip().split(',')
        for j in range(len(xs)-1):
            if xs[j] not in d:
                d[xs[j]] = []
    f.close()
    f = open(file,encoding="UTF-8")
    f.readline()
    for i in f:
        x = "".join(i.strip().split("\n"))
        xs = x.strip().split(',')
        if xs[2] == "amici" and (xs[1] not in d[xs[0]] or xs[0] not in d[xs[1]]):
            d[xs[0]].append(xs[1])
            d[xs[1]].append(xs[0])
        elif xs[2] == "nemici":
            if xs[1] in d[xs[0]] or xs[0] in d[xs[1]]:
                d[xs[0]].remove(xs[1])
                d[xs[1]].remove(xs[0])
        d[xs[0]].sort()
        d[xs[1]].sort()
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
