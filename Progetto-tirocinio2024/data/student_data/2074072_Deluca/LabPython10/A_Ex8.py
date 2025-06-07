def A_Ex8(file):
    f=open(file,encoding="UTF-8")
    S=f.readline()
    s=f.read()
    l=s.strip().split("\n")
    l1=[]
    for elem in l:
        l1.append(elem.strip().split(","))
    d={}
    for elem in l1:
        d[elem[0]]=[]
        d[elem[1]]=[]
    for elem in l1:
        if elem[2]=="amici":
            if elem[1] not in d[elem[0]]:
                d[elem[0]].append(elem[1])
                d[elem[0]].sort()
                if elem[0] not in d[elem[1]]:
                    d[elem[1]].append(elem[0])
                    d[elem[1]].sort()
        else:
            if elem[1] in d[elem[0]]:
                d[elem[0]].remove(elem[1])
                if elem[0] in d[elem[1]]:
                    d[elem[1]].remove(elem[0])
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
