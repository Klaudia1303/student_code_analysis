def A_Ex8(file):
    frenemies={}
    fin=open(file,encoding='UTF-8')
    next(fin)
    row=fin.readline()
    while len(row)>0:
        row=row.strip().split(',')
        frenemies[row[0]]=frenemies.get(row[0],[])
        frenemies[row[1]]=frenemies.get(row[1],[])
        if row[2]=='amici' and row[1] not in frenemies[row[0]] and row[0] not in frenemies[row[1]]:
            frenemies[row[0]]+=[row[1]]
            frenemies[row[1]]+=[row[0]]
        if row[2]=='nemici' and row[1] in frenemies[row[0]] and row[0] in frenemies[row[1]]:
            frenemies[row[0]].remove(row[1])
            frenemies[row[1]].remove(row[0])
        row=fin.readline()
    for i in frenemies.values():
        i.sort()
    
    return frenemies
        
        
    
    
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
