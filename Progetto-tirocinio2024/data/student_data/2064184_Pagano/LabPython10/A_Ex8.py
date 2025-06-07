def A_Ex8(file):
    d = {}
    with open(file, encoding="UTF-8") as f:
        rows = f.readlines()
        i = 1
        while i < len(rows):
            data = rows[i].strip().split(",")
            name1 = data[0]
            name2 = data[1]
            relationship = data[2]

            if relationship == "amici":
                if name1 in d:
                    if name2 not in d[name1]:
                        d[name1].append(name2)
                else:
                    d[name1] = [name2]

                if name2 in d:
                    if name1 not in d[name2]:
                        d[name2].append(name1)
                else:
                    d[name2] = [name1]

                d[name1].sort()
                d[name2].sort()
            else:
                if name1 in d and name2 in d[name1]:
                    d[name1].remove(name2)
                if name2 in d and name1 in d[name2]:
                    d[name2].remove(name1)

            i += 1
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
