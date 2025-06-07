def A_Ex8(file):
    f=open(file,encoding='UTF-8')
    fr=f.readlines()
    f.close()
    d={}
    for i in range(1,len(fr)):
        fr[i]=fr[i].replace(' ','').strip().split(',')
        if fr[i][2]=='amici':
            for j in range(2):
                if fr[i][j] in d:
                    if fr[i][1-j] not in d[fr[i][j]]:
                        d[fr[i][j]].append(fr[i][1-j])
                        d[fr[i][j]].sort()
                else:
                    d[fr[i][j]]=[fr[i][1-j]]
        elif fr[i][2]=='nemici':
            for j in range(2):
                if fr[i][j] in d:
                    if fr[i][1-j] in d[fr[i][j]]:
                        d[fr[i][j]].remove(fr[i][1-j])
                else:
                    d[fr[i][j]]=[fr[i][1-j]]
    
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
