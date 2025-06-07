def A_Ex3(fileName):
    f=open(fileName, encoding="UTF-8")
    fin=f.readlines()
    f.close()
    mat=list()
    materie=set()
    for i in range(1, len(fin)):
        s=fin[i].strip().split(',')
        if int(s[1])>=29:
            mat.append(s[2])
    for elem in mat:
        print(elem)
        n=mat.count(elem)
        if n>=2:
            materie.add(elem)
    return materie
    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun
    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"], {'Fisica'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"], set())
    counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"], {'Ricerca Operativa','Analisi'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"], {'Basi di Dati'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"], set())

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
