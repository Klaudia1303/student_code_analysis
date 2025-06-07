def A_Ex8(file):
    d={}
    file=open(file,'r',encoding='UTF-8')
    parametri=file.readline()
    for line in file:
        line=line.strip().split(',')
        d[line[1]]=d.get(line[1],[])
        d[line[0]]=d.get(line[0],[])      
        if line[2]=='amici':
            if line[1] in d[line[0]] and line[0] in d[line[1]]:
                d[line[1]]=d[line[1]]
                d[line[0]]=d[line[0]]
            else:
                d[line[0]]=d[line[0]]+[line[1]]
                d[line[1]]=d[line[1]]+[line[0]]
        if line[2]=='nemici':
            if line[1] in d[line[0]] and line[0] in d[line[1]]:
                d[line[0]].remove(line[1])
                d[line[1]].remove(line[0])
            
            
    for key in d:
        d[key].sort()
        
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
