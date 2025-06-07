def A_Ex8(file):
    d = {}
    l = []
    la = []
    f = open(file, encoding = "UTF-8")
    for i in f:
        i = i.strip().split(",")
        l.append(i)
    for i in range(1, len(l)):
        for j in range(2):
            if l[i][j] not in d:
                if l[i][j] == l[i][0]:
                    if l[i][2] == "amici":
                        la.append(l[i][1])
                elif l[i][j] == l[i][1]:
                    if l[i][2] == "amici":
                        la.append(l[i][0])
                d[l[i][j]] = la
                la = []
            else:
                la = d.get(l[i][j])
                if l[i][j] == l[i][0]:
                    if l[i][2] == "amici" and l[i][1] not in la:
                        la.append(l[i][1])
                    elif l[i][2] == "nemici" and l[i][1] in la:
                        la.remove(l[i][1])
                elif l[i][j] == l[i][1]:
                    if l[i][2] == "amici" and l[i][0] not in la:
                        la.append(l[i][0])
                    elif l[i][2] == "nemici" and l[i][0] in la:
                        la.remove(l[i][0])
                d[l[i][j]] = la
                la = []
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
