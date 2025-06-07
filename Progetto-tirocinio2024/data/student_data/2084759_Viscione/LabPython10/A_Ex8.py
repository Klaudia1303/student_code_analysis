def A_Ex8(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    fin=open(file, encoding="UTF-8")
    dizionario={}
    fin.readline()
    for r in fin:
        r=r.strip().split(",")
        if r[0] not in dizionario:
            dizionario[r[0]]=[]
        if r[1] not in dizionario:
            dizionario[r[1]]=[]
        if r[2]=="amici":
            if r[1] not in dizionario[r[0]]:
                dizionario[r[0]].append(r[1])
                dizionario[r[0]].sort()
            if r[0] not in dizionario[r[1]]:
                dizionario[r[1]].append(r[0])
                dizionario[r[1]].sort()
        elif r[2]=="nemici":
            if r[1] in dizionario[r[0]]:
                dizionario[r[0]].remove(r[1])
            if r[0] in dizionario[r[1]]:
                dizionario[r[1]].remove(r[0])
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
