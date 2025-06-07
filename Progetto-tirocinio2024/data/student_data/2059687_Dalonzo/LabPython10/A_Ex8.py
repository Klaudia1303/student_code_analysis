def A_Ex8(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    amicizie = {}
    rels = open(file, 'r',encoding='UTF-8')
    rels.readline()
    for rel in rels:
        values = rel.strip().split(',')
        amicizie[values[0]] = []
        amicizie[values[1]] = []

    rels = open(file, 'r',encoding='UTF-8')
    rels.readline()
    for rel in rels:
        values = rel.strip().split(',')
        if(values[2] == 'amici'):
            if(values[0] not in amicizie):
                amicizie[values[0]] = [values[1]]
            else:
                if(values[1] not in amicizie[values[0]]):
                    amicizie[values[0]].append(values[1])
            if(values[1] not in amicizie):
                amicizie[values[1]] = [values[0]]
            else:
                if(values[0] not in amicizie[values[1]]):
                    amicizie[values[1]].append(values[0])
        else:
            if(values[0] in amicizie):
                if(values[1] in amicizie[values[0]]):
                    amicizie[values[0]].remove(values[1])
            if(values[1] in amicizie):
                if(values[0] in amicizie[values[1]]):
                    amicizie[values[1]].remove(values[0])
        
    rels.close()
    for key in amicizie:
        amicizie[key].sort()

    return amicizie
    # lista.pop(amico) per amico diventato nemico
    # lista.append( amico) per il nuovo amico
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
