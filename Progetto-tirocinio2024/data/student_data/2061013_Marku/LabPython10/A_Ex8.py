def A_Ex8(file):
    d={}
    f=open(file, encoding='UTF-8')
    s=f.readline()
    r=f.readlines()
    for riga in r:
        dati=riga.strip().split(',')
        d[dati[0]]=[]
        d[dati[1]]=[]
    for riga in r:
        dati=riga.strip().split(',')
        if dati[2]=='amici' and dati[1] not in d[dati[0]]:
            d[dati[0]].append(dati[1])
        if dati[2]=='amici' and dati[0] not in d[dati[1]]:
            d[dati[1]].append(dati[0])
        if dati[2]=='nemici' and dati[1] in d[dati[0]]:
            d[dati[0]].remove(dati[1])
        if dati[2]=='nemici' and dati[0] in d[dati[1]]:
            d[dati[1]].remove(dati[0])
        d[dati[0]].sort()
        d[dati[1]].sort()
    f.close()
    return d





    
   # """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
    
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
