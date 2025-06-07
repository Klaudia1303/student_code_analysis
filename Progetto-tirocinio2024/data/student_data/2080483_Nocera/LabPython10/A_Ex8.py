def A_Ex8(file):
    d={}
    fin=open(file,encoding="UTF-8")
    f1=fin.readline().strip().split(",")
    for riga in fin:
        r=riga.strip().split(",")
        if r[2]=="amici":
            if r[0] not in d:
                d[r[0]]=[r[1]]
            else:
                if r[1] not in d[r[0]]:
                    d[r[0]].append(r[1])
                    d[r[0]]=sorted(d[r[0]])

            if r[1] not in d:
                d[r[1]]=[r[0]]
            else:
                if r[0] not in d[r[1]]:
                    d[r[1]].append(r[0])
                    d[r[1]]=sorted(d[r[1]])

            
        elif r[2]=="nemici":
            print("ciao")
            
            if d.get(r[0],1) != 1 and r[1] in d[r[0]]:
                   val=list(d[r[0]])
                   val.remove(r[1])
                   d[r[0]]=val
                
            if d.get(r[1],1) != 1 and r[0] in d[r[1]]:
                    val1=list(d[r[1]])
                    val1.remove(r[0])
                    d[r[1]]=val1
    fin.close()                        
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
