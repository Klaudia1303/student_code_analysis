def A_Ex8(file):
    f=open(file,'r',encoding="UTF-8")
    f.readline()
    testo=f.readlines()
    f.close()
    diz={}
    for riga in testo:
        riga=riga.strip().split(',')
        diz[riga[0]]=diz.get(riga[0],[])
        diz[riga[1]]=diz.get(riga[1],[])
        if riga[2]=='amici':
            if riga[1] not in diz[riga[0]]:
                diz[riga[0]]=diz.get(riga[0],[])+[riga[1]]
                diz[riga[1]]=diz.get(riga[1],[])+[riga[0]]
        else:
            if riga[1] in diz[riga[0]]:
                diz[riga[0]].remove(riga[1])
                diz[riga[1]].remove(riga[0])
    for key in diz:
        diz[key].sort()
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
