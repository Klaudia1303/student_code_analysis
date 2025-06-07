def A_Ex8(file):
    f=open(file,encoding=('UTF-8'))
    r=f.readlines()
    l=[]
    d={}
    for i in r:
        i=i.strip().split(',')
        l.append(i)
    l.remove(l[0])
    for i in l:
        for j in range(2):
            d[i[j]]=[] 
    for i in l:
        for j in range(len(i)):
            if i[2]=='amici':
                if i[1] not in d[i[0]]:
                    d[i[0]].append(i[1])
                    d[i[0]].sort()
                    
                elif i[0] not in d[i[1]]:
                    d[i[1]].append(i[0])
                    d[i[1]].sort()
                    break
                
            else:
                if i[1] in d[i[0]]:
                    
                    d[i[0]].remove(i[1])
                    d[i[0]].sort()
                    
                elif i[0] in d[i[1]]:
                    d[i[1]].remove(i[0])
                    d[i[1]].sort()
                    break
           
    
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
