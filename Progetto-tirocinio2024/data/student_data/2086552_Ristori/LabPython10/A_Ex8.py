def A_Ex8(file):
    d={}
    fin=open(file,"r",encoding="UTF-8")
    riga=fin.readline()
    riga=fin.readline()
    while len(riga)>1:
        riga=riga.strip().split(",")
        if riga[2]=="amici":
            if riga[0] not in d:
                d[riga[0]]={riga[1]}
            else:
                d[riga[0]]=d[riga[0]]|{riga[1]}
            if riga[1] not in d:
                d[riga[1]]={riga[0]}
            else:
                d[riga[1]]=d[riga[1]]|{riga[0]}
        if riga[2]=="nemici":
            if riga[0] not in d:
                d[riga[0]]=set()
            else:
                d[riga[0]]=d[riga[0]]-{riga[1]}
            if riga[1] not in d:
                d[riga[1]]=set()
            else:
                d[riga[1]]=d[riga[1]]-{riga[0]}
        riga=fin.readline()
    for v in d.keys():
        d[v]=list(d[v])
    for v in d.values():
        v.sort()
    fin.close()
    return d














    #"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
    
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
