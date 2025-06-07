def A_Ex8(file):
    f=open(file,encoding='UTF-8')
    d={}
    l=[]
    for riga in f:
        l.append(riga.strip().split(','))
    l.remove(l[0])
    for i in l:
        if i[2]=='amici':
            if i[0] not in d:
                d[i[0]]=[]
                d[i[0]].append(i[1])
            else:
                if i[1] not in d[i[0]]:
                    d[i[0]].append(i[1])
            if i[1] not in d:
                d[i[1]]=[]
                d[i[1]].append(i[0])
            else:
                if i[0] not in d[i[1]]:
                    d[i[1]].append(i[0])
        elif i[2]=='nemici':
            if i[0] in d:
                if i[1] in d[i[0]]:
                    d[i[0]].remove(i[1])
            if i[1] in d:
                if i[0] in d[i[1]]:
                    d[i[1]].remove(i[0])
    for key in d:
        d[key].sort()
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
