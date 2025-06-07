def A_Ex8(file):
    f=open(file,"r",encoding="UTF-8")
    f.readline()
    d={}
    for line in f:
        lista=list()
        l=line.strip().split(",")
        if l[0] not in d:
            d[l[0]]=[]
        if l[1] not in d:
            d[l[1]]=[]

        if l[2]=="amici":
            lista=d.get(l[0])
            if l[1] not in lista:
                lista.append(l[1])
            lista.sort()
            d[l[0]]=lista
            lista=list()
            
            lista=d.get(l[1])
            if l[0] not in lista:
                lista.append(l[0])
            lista.sort()
            d[l[1]]=lista

        if l[2]=="nemici":
            lista=d.get(l[0])
            if l[1] in lista:
                lista.remove(l[1])
            lista.sort()
            d[l[0]]=lista

            lista=list()

            lista=d.get(l[1])
            if l[0] in lista:
                lista.remove(l[0])
            lista.sort()
            d[l[1]]=lista
            
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
