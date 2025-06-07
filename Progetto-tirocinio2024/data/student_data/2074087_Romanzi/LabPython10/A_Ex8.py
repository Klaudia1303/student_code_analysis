def A_Ex8(file):

    f=open(file,encoding="UTF-8")
    ls=[]
    lt=[]
    lp=[]
    ds={}
    for i in f:
        i=i.strip().split(",")
        ls.append(i)
    for j in range(1,len(ls)):
        if ls[j][2]=="amici":
            if ls[j][0] not in ds and ls[j][1] not in ds:
                ds[ls[j][0]]=[ls[j][1]]
                ds[ls[j][1]]=[ls[j][0]]
            elif ls[j][0] not in ds and ls[j][1] in ds:
                ds[ls[j][0]]=[ls[j][1]]
                lt=ds[ls[j][1]]
                lt.append(ls[j][0])
                ds[ls[j][1]]=lt
            elif ls[j][0] in ds and ls[j][1] not in ds:
                ds[ls[j][1]]=[ls[j][0]]
                lt=ds[ls[j][0]]
                lt.append(ls[j][1])
                ds[ls[j][0]]=lt
            else:
                if ls[j][0] not in ds[ls[j][1]] and ls[j][1] not in ds[ls[j][0]]:
                    lt=ds[ls[j][1]]
                    lt.append(ls[j][0])
                    ds[ls[j][1]]=lt
                    lt=ds[ls[j][0]]
                    lt.append(ls[j][1])
                    ds[ls[j][0]]=lt
        else:
            if ls[j][0] not in ds and ls[j][1] not in ds:
                ds[ls[j][0]]=[]
                ds[ls[j][1]]=[]
            elif ls[j][0] not in ds and ls[j][1] in ds:
                ds[ls[j][0]]=[]
                ds[ls[j][1]]=[]
            elif ls[j][0] in ds and ls[j][1] not in ds:
                ds[ls[j][0]]=[]
                ds[ls[j][1]]=[]
            else:
                lt=ds[ls[j][0]]
                lp=ds[ls[j][1]]
                for z in range(len(lt)):
                    for k in range(len(lp)):
                        if lt[z]==ls[j][1] and lp[k]==ls[j][0]:
                            lt.remove(lt[z])
                            lp.remove(lp[k])
                            ds[ls[j][0]]=lt
                            ds[ls[j][1]]=lp
    for i in ds:
        if len(i)>0:
            lt=ds[i]
            lt.sort()
            ds[i]=lt
    f.close()
    return ds
    
    
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
