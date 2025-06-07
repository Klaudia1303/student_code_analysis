def A_Ex8(file):
    f = open(file)
    r = f.readlines()
    dizionario = {}
    lista = []
    for s in range(1, len(r)):
        r[s] = r[s].strip().split(",")
        if r[s][0] not in dizionario.keys():
            lista = []
            lista.append(r[s][1])
            lista.sort()
            dizionario.update({r[s][0]:lista})
        else:
            if r[s][1] not in dizionario[r[s][0]]:
                dizionario[r[s][0]].append(r[s][1])
                dizionario[r[s][0]].sort()
        if r[s][1] not in dizionario.keys():
            lista = []
            lista.append(r[s][0])
            lista.sort()
            dizionario.update({r[s][1]:lista})
        else:
            if r[s][0] not in dizionario[r[s][1]]:
                dizionario[r[s][1]].append(r[s][0])
                dizionario[r[s][1]].sort()
        if r[s][2] == "nemici":
            if r[s][1] in dizionario[r[s][0]]:
                dizionario[r[s][0]].remove(r[s][1])
            if r[s][0] in dizionario[r[s][1]]:
                dizionario[r[s][1]].remove(r[s][0])
                
    return dizionario            
            
    
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
