def A_Ex8(file):
    x = open(file,'r',encoding='UTF-8')
    y = x.readline()
    
    d = {}
    a = []

    for i in x:
        i = i.strip().split(',')

        if i[2] == 'amici':
            if i[0] not in d:
                a.append(i[1])
                d[i[0]] = a
                a = []
            else:
                if i[1] not in d[i[0]]:
                    a.append(i[1])
                    d[i[0]] = d[i[0]]+a
                    d[i[0]].sort()
                    a = []
                
            if i[1] not in d:
                a.append(i[0])
                d[i[1]] = a
                a = []
            else:
                if i[0] not in d[i[1]]:
                    a.append(i[0])
                    d[i[1]] = d[i[1]]+a
                    d[i[1]].sort()
                    a = []
                    

        elif i[2] == 'nemici':
            if i[0] in d:
                if i[1] in d[i[0]]:
                    d[i[0]].remove(i[1])

            if i[1] in d:
                if i[0] in d[i[1]]:
                    d[i[1]].remove(i[0])

    return d     

    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
    
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
