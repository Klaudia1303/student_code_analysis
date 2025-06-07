def A_Ex3(fileName):
    f=open(fileName,'r',encoding='UTF-8')
    l=[]
    i=set()
    res=set()
    f.readline()
    for line in f:
        s=line.strip().split(',')
        l.append(s)
    f.close()
    for e in l:
        i.add(e[2])
    for el in i:
        k=0
        for elem in l:
            if elem[2]==el and int(elem[1])>28:
                k+=1
        if k>1:
            res.add(el)
    
    return res
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

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
