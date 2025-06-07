def A_Ex8(file):
    f=open(file)
    f.readline()
    d={}
    for riga in f:
        riga=riga.strip().split(',')
        if riga[2]=='amici':
            d[riga[0]]=d.get(riga[0],[])
            if riga[1] not in d[riga[0]]:
                d[riga[0]].append(riga[1])
            d[riga[1]]=d.get(riga[1],[])
            if riga[0] not in d[riga[1]]:
                d[riga[1]].append(riga[0])
        elif riga[2]=='nemici':
            d[riga[0]]=d.get(riga[0],[])
            if riga[1] in d[riga[0]]:
                d[riga[0]].remove(riga[1])
            d[riga[1]]=d.get(riga[1],[])
            if riga[0] in d[riga[1]]:
                d[riga[1]].remove(riga[0])
    for k in d:
        d[k].sort()
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
