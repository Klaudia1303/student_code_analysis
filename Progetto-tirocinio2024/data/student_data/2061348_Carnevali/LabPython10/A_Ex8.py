def A_Ex8(file):
    a=open(file,encoding="UTF-8")
    b=a.readlines()
    d={}
    for n in range(1,len(b)):
        ln=b[n].strip().split(",")
        for m in (0,1):
            x=[]
            for l in range(1,len(b)):
                ll=b[l].strip().split(",")
                if ll[2]=="amici":
                    if ll[0]==ln[m]and ll[1]not in x:
                        x.append(ll[1])
                    elif ll[1]==ln[m]and ll[0]not in x:
                        x.append(ll[0])
                if ll[2]=="nemici":
                    if ll[0]==ln[m]and ll[1]in x:
                        x.remove(ll[1])
                    elif ll[1]==ln[m]and ll[0]in x:
                        x.remove(ll[0])
            x.sort()
            d[ln[m]]=x
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
