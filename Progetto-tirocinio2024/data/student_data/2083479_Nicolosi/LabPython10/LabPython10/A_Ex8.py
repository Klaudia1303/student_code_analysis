def A_Ex8(file):
    fin=open(file,encoding='UTF-8')
    d={}
    campi=fin.readline()
    campi=campi.strip().split(',')
    riga=fin.readline()
    while len(riga)>0:
        riga=riga.strip().split(',')
        amico1=riga[0]
        amico2=riga[1]
        if amico1 not in d:
            relazione=riga[2]
            if relazione=='amici':
                d[amico1]={amico2}
        if amico2 not in d:
            relazione=riga[2]
            if relazione=='amici':
                d[amico2]={amico1}
        if amico1 in d:
            relazione=riga[2]
            if relazione=='amici':
                d[amico1].add(amico2)
            elif amico2 in d[amico1]:
                d[amico1].discard(amico2)
        if amico2 in d:
            relazione=riga[2]
            if relazione=='amici':
                d[amico2].add(amico1)
            elif amico1 in d[amico2]:
                d[amico2].discard(amico1)
        riga=fin.readline()
    for key in d:
        d[key]=list(d[key])
        d[key].sort()
    fin.close()
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
