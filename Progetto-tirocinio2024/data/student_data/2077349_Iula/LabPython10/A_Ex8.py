def A_Ex8(file):
    f=open(file,'r',encoding="UTF-8")
    lfile=[]
    d={}
    nomi=[]
    for el in f:
        l=el.strip().split(',')
        lfile.append(l)
    for j in range(1,len(lfile)):
            if d.get(lfile[j][0],0)==0:
                d[lfile[j][0]]=[]
            if d.get(lfile[j][1],0)==0:
                d[lfile[j][1]]=[]
            if lfile[j][2]=="amici":
                if lfile[j][1] not in d[lfile[j][0]]:
                    d[lfile[j][0]].append(lfile[j][1])
                else:
                    d[lfile[j][0]].remove(lfile[j][1])
                    d[lfile[j][0]].append(lfile[j][1])
                if lfile[j][0] not in d[lfile[j][1]]:
                    d[lfile[j][1]].append(lfile[j][0])
                else:
                    d[lfile[j][1]].remove(lfile[j][0])
                    d[lfile[j][1]].append(lfile[j][0])
                    print(d[lfile[j][0]],d[lfile[j][1]])
            if lfile[j][2]=="nemici":
                    if lfile[j][1] in d[lfile[j][0]]:
                        d[lfile[j][0]].remove(lfile[j][1])
                    if lfile[j][0] in d[lfile[j][1]]:
                        d[lfile[j][1]].remove(lfile[j][0])
                    print(d[lfile[j][0]],d[lfile[j][1]])
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
