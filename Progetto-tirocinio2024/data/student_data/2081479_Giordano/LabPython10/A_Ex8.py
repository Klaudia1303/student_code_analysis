def A_Ex8(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    with open(file, encoding='UTF-8') as txt:
        line=txt.readline().strip().split(',')
        line=txt.readline().strip().split(',')
        fDic={}
        fList=[]
        while line != ['']:
            fDic[line[0]]=[]
            fDic[line[1]]=[]
            fList.append(line)
            line=txt.readline().strip().split(',')

    for cLine in fList:
        if cLine[2]=='amici':
            if cLine[1] not in fDic[cLine[0]]:
                fDic[cLine[0]].append(cLine[1])
            if cLine[0] not in fDic[cLine[1]]:
                fDic[cLine[1]].append(cLine[0])
        if cLine[2]=='nemici':
            if cLine[0] in fDic[cLine[1]]:
                fDic[cLine[1]].remove(cLine[0])
            if cLine[1] in fDic[cLine[0]]:
                fDic[cLine[0]].remove(cLine[1])
    for item in fDic:
        fDic[item].sort()
    return fDic
    
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
