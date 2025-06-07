def A_Ex8(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(file,encoding="UTF-8")
    next(f)
    amici={}
    l=f.read().strip().splitlines()
    for i in range(0,len(l)):
        l[i]=l[i].split(",")
    for i in range (0,len(l)):
        if "amici" in l[i]:
            if l[i][0] in amici:
                if l[i][1] not in amici[l[i][0]]:
                    amici[l[i][0]].append(l[i][1])
                    amici[l[i][0]].sort()
            else:
                amici[l[i][0]]=[l[i][1]]

            if l[i][1] in amici:
                if l[i][0] not in amici[l[i][1]]:
                    amici[l[i][1]].append(l[i][0])
                    amici[l[i][1]].sort()
            else:
                amici[l[i][1]]=[l[i][0]]
            
        else:
            if l[i][0] not in amici:
                amici[l[i][0]]=[]
            else:
                if l[i][0] in amici[l[i][1]]:
                    amici[l[i][1]].remove(l[i][0])
            if l[i][1] in amici[l[i][0]]:
                amici[l[i][0]].remove(l[i][1])

            if l[i][1] not in amici:
                amici[l[i][1]]=[] 
            else:
                if l[i][0] in amici[l[i][1]]:
                    amici[l[i][1]].remove(l[i][0])
            if l[i][1] in amici[l[i][0]]:
                    amici[l[i][0]].remove(l[i][1])
            

    return amici
    
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
