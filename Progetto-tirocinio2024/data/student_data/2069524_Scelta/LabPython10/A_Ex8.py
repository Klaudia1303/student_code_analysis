def A_Ex8(file):
    d={}
    f=open(file,'r',encoding='UTF-8')
    _=f.readline()
    
    
    for line in f.readlines():
        (nome1,nome2,relazione)=line.strip().split(",")
      
        if relazione=='amici':
            d.setdefault(nome1,[nome2]).append(nome2)
            d[nome1]=sorted(list(set(d[nome1])))
           
            d.setdefault(nome2,[nome1]).append(nome1)
            d[nome2]=sorted(list(set(d[nome2])))

        elif relazione=='nemici':
            if nome1 in d and nome2 in d[nome1]:
                d[nome1].remove(nome2)
            
            if nome2 in d and nome1 in d[nome2]:
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
