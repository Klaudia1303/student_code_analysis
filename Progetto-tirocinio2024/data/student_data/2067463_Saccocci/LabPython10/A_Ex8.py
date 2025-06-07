def A_Ex8(file):
    f=open(file,'r',encoding='UTF-8')
    l=[]
    d={}
    prima=f.readline()
    for riga in f:
        l.append(riga.strip().split(','))
    for i in range(len(l)):
        nome1=l[i][0]
        nome2=l[i][1]
        rel=l[i][2].strip()
        if nome1 not in d:
            if rel=='amici':
                d[nome1]=[nome2]
            elif rel=='nemici':
                d[nome1]=[]
        else:
            if rel=='amici':
                if nome2 not in d[nome1]:
                    d[nome1].append(nome2)
                    d[nome1].sort()
            elif rel=='nemici':
                if nome2 in d[nome1]:
                    d[nome1].remove(nome2)
        if nome2 not in d:
            if rel=='amici':
                d[nome2]=[nome1]
            elif rel=='nemici':
                d[nome2]=[] 
        else:
            if rel=='amici':
                if nome1 not in d[nome2]:
                    d[nome2].append(nome1)
                    d[nome2].sort()
            elif rel=='nemici':
                if nome1 in d[nome2]:
                    d[nome2].remove(nome1)
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
