def A_Ex8(file):
    
    f=open(file,'r',encoding='UTF-8')
    first=f.readline()
    d={}
    l=[]
    
    for riga in f:
        riga=riga.strip().split(',')
        
        if riga[2]=='amici':
            d[riga[0]]=d.get(riga[0], set())
            d[riga[0]].add(riga[1])
            d[riga[1]]=d.get(riga[1], set())
            d[riga[1]].add(riga[0])
            
        if riga[2]=='nemici':
            d[riga[0]]=d.get(riga[0], set())
            d[riga[0]].discard(riga[1])
            d[riga[1]]=d.get(riga[1], set())
            d[riga[1]].discard(riga[0])
            
    for k in d:
        lis=list(d[k])
        lis.sort()
        d[k]=lis
        
    f.close()
    
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
