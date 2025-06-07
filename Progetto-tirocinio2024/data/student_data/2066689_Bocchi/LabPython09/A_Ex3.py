def A_Ex3(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f= open(fileName,encoding="UTF-8")
    butta=f.readline()
    sv=[]
    insiemeFinale=set()
    lista=[]
    for el in f:
        el=el.strip().split(',')
        sv.append(el)
    for els in sv:
        if int(els[1])>=29:
            lista.append(els[2])
    for i in range(len(lista)):
        if lista.count(lista[i])>=2:
            insiemeFinale.add(lista[i])
            f.close()
    return insiemeFinale

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
