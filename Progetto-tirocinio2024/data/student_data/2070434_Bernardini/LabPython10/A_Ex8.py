def A_Ex8(file):
    a=open(file, 'r', encoding='UTF-8')
    sv=[]
    d={}
    for elem in a:
        elem=elem.strip().split(',')
        sv.append(elem)
    for i in range(1,len(sv)):
        if sv[i][0] not in d:
            d[sv[i][0]]=list()
        if sv[i][1] not in d:
            d[sv[i][1]]=list()
        if sv[i][2]=='amici' and sv[i][0] not in d[sv[i][1]] and sv[i][1] not in d[sv[i][0]]:
                d[sv[i][1]].append(sv[i][0])
                d[sv[i][0]].append(sv[i][1])
                d[sv[i][0]].sort()
                d[sv[i][1]].sort()
        if sv[i][2]=='nemici' and sv[i][0] in d[sv[i][1]] and sv[i][1] in d[sv[i][0]] :
                d[sv[i][1]].remove(sv[i][0])
                d[sv[i][0]].remove(sv[i][1])
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
