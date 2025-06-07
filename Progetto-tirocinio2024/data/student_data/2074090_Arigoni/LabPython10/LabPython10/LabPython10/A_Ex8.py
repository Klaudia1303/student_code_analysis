def A_Ex8(file):
    f=open(file,"r",encoding="utf-8")
    sol=[]
    d={}
    for elem in f:
        elem=elem.strip().split(",")
        sol.append(elem)
    for i in range(1,len(sol)):
        if sol[i][0] not in d:
            d[sol[i][0]]=[]
        if sol[i][1] not in d:
            d[sol[i][1]]=[]
    for i in range(1,len(sol)):
        if sol[i][2]=="amici" and sol[i][1] not in d[sol[i][1]] and sol[i][0] not in d[sol[i][1]] and sol[i][1] not in d[sol[i][0]] and sol[i][0] not in d[sol[i][0]]:
            d[sol[i][0]].append(sol[i][1])
            d[sol[i][1]].append(sol[i][0])
            d[sol[i][0]].sort()
            d[sol[i][1]].sort()

            
        if sol[i][2]=="nemici" and len(d[sol[i][0]])!=0 and len(d[sol[i][1]])!=0:
            d[sol[i][0]].remove(sol[i][1])
            d[sol[i][1]].remove(sol[i][0])
            




                
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
