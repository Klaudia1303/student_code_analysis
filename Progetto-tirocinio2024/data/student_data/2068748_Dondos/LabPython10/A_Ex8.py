def A_Ex8(file):
    f=open(file,"r",encoding="UTF-8")
    f.readline()
    l=f.readlines()
    lines=[]
    for line in l:
        lines.append(line.strip().split(","))
    print(lines)
    d={}
    for rel in lines:
        if rel[2]=='amici':
            if rel[0] not in d:
                d[rel[0]]=[]
            if rel[1] not in d:
                d[rel[1]]=[]
            if rel[1] not in d[rel[0]]:
                d[rel[0]].append(rel[1])
            if rel[0] not in d[rel[1]]:
                d[rel[1]].append(rel[0])

        if rel[2]=='nemici':
            if rel[0] not in d:
                d[rel[0]]=[]
            if rel[1] not in d:
                d[rel[1]]=[]
            if rel[0] in d[rel[1]]:
                d[rel[1]].remove(rel[0])
            if rel[1] in d[rel[0]]:
                d[rel[0]].remove(rel[1])
        d[rel[0]].sort()
        d[rel[1]].sort()
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
