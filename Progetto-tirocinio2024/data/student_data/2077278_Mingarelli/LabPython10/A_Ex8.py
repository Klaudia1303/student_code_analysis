def A_Ex8(file):
    d={}
    f=open(file,encoding='UTF-8')
    f.readline()
    relazione=f.readline().strip().split(',')
    while len(relazione)>0 and relazione!=['']:
        if relazione[0] not in d:
            d[relazione[0]]=[]
        if relazione[1] not in d:
            d[relazione[1]]=[]
        if relazione[2]=='amici':
            if relazione[0] not in d[relazione[1]]:
                d[relazione[0]].append(relazione[1])
                d[relazione[1]].append(relazione[0])
                d[relazione[0]].sort()
                d[relazione[1]].sort()
        if relazione[2]=='nemici':
            if relazione[0] in d[relazione[1]]:
                d[relazione[0]].remove(relazione[1])
                d[relazione[1]].remove(relazione[0])
        relazione=f.readline().strip().split(',')
        
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
