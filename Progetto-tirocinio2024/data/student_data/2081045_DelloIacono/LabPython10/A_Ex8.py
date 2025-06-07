def A_Ex8(file):
    f=open(file)
    diz={}
    lista=[]
    riga1=f.readline()
    righe=f.readlines()
    for i in righe:
        parole=i.strip().split(',')
        if parole[2]=='amici':
            if not parole[0] in diz:
                diz[parole[0]]=[]
            if not parole[1] in diz:
                diz[parole[1]]=[]
            if parole[1] not in diz[parole[0]]:
                diz[parole[0]].append(parole[1])
            if parole[0] not in diz[parole[1]]:
                diz[parole[1]].append(parole[0])
        if parole[2]=='nemici':
            if not parole[0] in diz:
                diz[parole[0]]=[]
            if not parole[1] in diz:
                diz[parole[1]]=[]
            if parole[1] in diz[parole[0]]:
                diz[parole[0]].remove(parole[1])
            if parole[0] in diz[parole[1]]:
                diz[parole[1]].remove(parole[0])
        diz[parole[0]].sort()
        diz[parole[1]].sort()
    return diz
            
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
