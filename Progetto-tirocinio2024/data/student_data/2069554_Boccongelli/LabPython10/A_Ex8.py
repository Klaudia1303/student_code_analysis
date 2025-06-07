def A_Ex8(file):
    d = {}
    f = open(file, 'r', encoding='UTF-8')
    t = f.read().split('\n')
    f.close()
    for i in range(1, len(t)):
        s = t[i].replace(' ', '', t[i].count(' ')).split(',')
        if (s != ['']):
            if (s[2] == 'amici'):
                for j in range(2):
                    if s[j] in d:
                        if (s[1 - j] not in d[s[j]]):
                            d[s[j]].append(s[1 - j])
                            d[s[j]].sort()
                    else:
                        d[s[j]] = [s[1 - j]]
            elif (s[2] == 'nemici'):
                for j in range(2):
                    if s[j] in d:
                        if (s[1 - j] in d[s[j]]):
                            d[s[j]].remove(s[1 - j])
                    else:
                        d[s[j]] = []
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
