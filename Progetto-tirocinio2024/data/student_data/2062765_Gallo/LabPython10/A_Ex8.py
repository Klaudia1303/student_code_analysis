def A_Ex8(file):
    f=open(file,"r",encoding="utf-8")
    d={}
    f.readline()
    for riga in f:
        dati=riga.strip().split(",")
        nome1=(dati[0])
        nome2=(dati[1])
        relazione=(dati[2])
        if relazione=="amici":
            if nome1 not in d and nome2 not in d:
                l=[]
                l.append(nome2)
                l2=[]
                l2.append(nome1)
                d[nome1]=l
                d[nome2]=l2
            elif nome1 in d and nome2 not in d:
                l=d.get(nome1)
                if nome2 not in l:
                    l.append(nome2)
                    l.sort()
                l2=[]
                l2.append(nome1)
                d[nome1]=l
                d[nome2]=l2
            elif nome1 not in d and nome2 in d:
                l=[]
                l.append(nome2)
                l2=d.get(nome2)
                if nome1 not in l2:
                    l2.append(nome1)
                    l2.sort()
                d[nome1]=l
                d[nome2]=l2
            elif nome1 in d and nome2 in d:
                l=d.get(nome1)
                if nome2 not in l:
                    l.append(nome2)
                    l.sort()
                l2=d.get(nome2)
                if nome1 not in l2:
                    l2.append(nome1)
                    l2.sort()
                d[nome1]=l
                d[nome2]=l2
        elif relazione=="nemici":
            if nome1 in d and nome2 in d:
                l=d.get(nome1)
                if nome2 in l:
                    l.remove(nome2)
                    l.sort()
                    l2=d.get(nome2)
                    l2.remove(nome1)
                    l2.sort()
                    d[nome1]=l
                    d[nome2]=l2
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
