def A_Ex8(file):
    f = open(file, encoding="UTF-8")
    f.readline()

    amici = {}

    for x in f:
        a1 = x.strip()
        a2 = a1.split(",")
        p1 = a2[0]
        p2 = a2[1]
        amicizia = (a2[2] == "amici")

        if amicizia:
            if p1 in amici:
                if not p2 in amici[p1]:
                    amici[p1].append(p2)
            else:
                amici[p1] = [p2]

            if p2 in amici:
                if not p1 in amici[p2]:
                    amici[p2].append(p1)
            else:
                amici[p2] = [p1]

        else:
            if p1 in amici:
                if p2 in amici[p1]:
                    amici[p1].remove(p2)
            else:
                amici[p1] = []

            if p2 in amici:
                if p1 in amici[p2]:
                    amici[p2].remove(p1)
            else:
                amici[p2] = []


    for k in amici:
        amici[k].sort()

    return amici
    
    
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
