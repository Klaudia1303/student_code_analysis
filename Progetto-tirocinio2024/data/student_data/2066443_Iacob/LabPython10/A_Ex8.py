def A_Ex8(file):
    o = open(file, 'r', encoding="UTF-8")
    o.readline()
    diz = {}
    
    for i in o:
        l = "".join(i.strip().split("\n"))
        s = l.strip().split(',')
        for k in range(len(s)-1):
            if s[k] not in diz:
                diz[s[k]] = []
    o.close()
    
    f = open(file, 'r', encoding="UTF-8")
    f.readline()
    for h in f:
        m = "".join(h.strip().split("\n"))
        t = m.strip().split(',')
        if t[2] == "amici":
            if t[1] not in diz[t[0]] or t[0] not in diz[t[1]]:
                diz[t[0]].append(t[1])
                diz[t[1]].append(t[0])
        elif t[2] == "nemici":
            if t[1] in diz[t[0]] or t[0] in diz[t[1]]:
                diz[t[0]].remove(t[1])
                diz[t[1]].remove(t[0])
        diz[t[0]].sort()
        diz[t[1]].sort()
    f.close()
    
    return diz
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
