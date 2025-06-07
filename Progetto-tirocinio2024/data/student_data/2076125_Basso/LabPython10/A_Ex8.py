def A_Ex8(file):
    f=open(file)
    d={}
    riga=f.readline()
    riga=f.readline()
    dati=riga.strip().split(',')
    while len(riga)>0:
        p1=dati[0]
        p2=dati[1]
        if dati[2]=='amici':
            if p1 not in d:
                d[p1]=set()
            if p2 not in d:
                d[p2]=set()
            d[p1].add(p2)
            d[p2].add(p1)
                

        elif dati[2]=='nemici':
            if p1 not in d:
                d[p1]=set()
            if p2 not in d:
                d[p2]=set()

            if p1 in d[p2]:
                d[p2].discard(p1)
            if p2 in d[p1]:
                d[p1].discard(p2)
        
        riga=f.readline()
        dati=riga.strip().split(',')

    for k in d:
            d[k]=list(d[k])
            d[k].sort()
    f.close()
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
