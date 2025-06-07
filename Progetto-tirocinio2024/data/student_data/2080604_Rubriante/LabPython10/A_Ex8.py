def A_Ex8(file):
    f=open(file,encoding="UTF-8")
    diz={}
    f.readline()
    for i in f:
        lis1=[]
        lis2=[]
        i=i.strip().split(",")
        if i[2]=="amici":
            if i[0] not in diz:
                diz[i[0]]=[]
            if i[1] not in diz:
                diz[i[1]]=[]
            if i[1] not in diz[i[0]]:
                diz[i[0]].append(i[1])
            if i[0] not in diz[i[1]]:
                diz[i[1]].append(i[0])
        else:
            if i[0] not in diz:
                diz[i[0]]=[]
            if i[1] not in diz:
                diz[i[1]]=[]
            if i[1] in diz[i[0]]:
                diz[i[0]].remove(i[1])
            if i[0] in diz[i[1]]:
                diz[i[1]].remove(i[0])
    for i in diz:
        diz[i].sort()
    return diz
    
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
