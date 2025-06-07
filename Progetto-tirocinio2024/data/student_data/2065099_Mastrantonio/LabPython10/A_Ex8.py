def A_Ex8(file):
    file = open(file, encoding = 'UTF-8')
    l = []
    for elem in file :
        elem = elem.strip().split(',')
        l.append(elem)
    l.remove(l[0])
    d= {}
    for riga in l :
        print(riga)
        for elem in riga[:2]:
            if elem not in d:
                d[elem] = []
    for riga in l:
        nome1 = riga[0]
        nome2 = riga[1]
        relaz = riga[2]
        lista1 = d[nome1]
        lista2 = d[nome2]
        if relaz == 'amici':
            if nome1 not in lista2:
                lista1.append(nome2)
                lista2.append(nome1)
                d[nome1] = lista1
                d[nome2] = lista2
            elif nome1 in lista2 :
                lista1.remove(nome2)
                lista2.remove(nome1)
                lista1.append(nome2)
                lista2.append(nome1)
                d[nome1] = lista1
                d[nome2] = lista2
        elif relaz == 'nemici':
            if nome2 in lista1:
                lista1.remove(nome2)
                lista2.remove(nome1)
                d[nome1] = lista1
                d[nome2] = lista2
    return(d)
    
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
